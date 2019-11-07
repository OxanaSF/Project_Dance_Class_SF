from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()



class User(db.Model):
    """Data model for User."""

#instances of User class will be stored in table users
    __tablename__ = 'users'

    """Columns and/or relationships"""

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    email = db.Column(db.String(100), nullable=False)

    bookmarked_classes = db.relationship('Class',
                                         secondary='bookmarks',
                                         backref='bookmarked_by')


    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"""
        <User
        user_id={self.user_id}
        email={self.email}>"""

                         


class Bookmark(db.Model):
    """Data model for Bookmark."""

    __tablename__ = 'bookmarks'

    bookmark_id = db.Column(db.Integer,
                       autoincrement=True,
                       primary_key=True)

    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.user_id'),
                        nullable=False)
    dance_class_id = db.Column(db.Integer,
                               db.ForeignKey('classes.class_id'), 
                               nullable=False)

    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"""
        <Bookmark
        bookmark_id={self.bookmark_id}
        user_id={self.user_id}
        class_id={self.class_id}>"""



class Rating(db.Model):
    """Data model for Rating."""

    __tablename__ = 'ratings'

    rating_id = db.Column(db.Integer,
                          autoincrement=True,
                          primary_key=True)

    score = db.Column(db.Integer, nullable=False)

    user_id = db.Column(db.Integer,
                        db.ForeignKey('users.user_id'),
                        nullable=False)
    class_id = db.Column(db.Integer,
                               db.ForeignKey('classes.class_id'), 
                               nullable=False)

    user = db.relationship('User', backref='ratings')
    dance_class = db.relationship('Class', backref='ratings')

    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"""
        <Rating 
        rating_id={self.rating_id} 
        score={self.score} 
        user_id={self.user_id} 
        class_id={self.class_id}>"""



class DanceStyle(db.Model):
    """Data model for DanceClass."""

    __tablename__ = 'dancestyles'

    dance_id = db.Column(db.Integer,
                       autoincrement=True,
                       primary_key=True)

    
    name = db.Column(db.String(200))

    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"""
        <DanceStyle 
        dance_id={self.dance_id} 
        name={self.name} >\n"""

    


class Class(db.Model):
    """Data model for DanceClass."""

    __tablename__ = 'classes'

    class_id = db.Column(db.Integer,
                       autoincrement=True,
                       primary_key=True)

    dance_id = db.Column(db.Integer, 
                        db.ForeignKey('dancestyles.dance_id'),
                        nullable=False)

    school_id = db.Column(db.Integer,
                          db.ForeignKey('schools.school_id'),
                          nullable=False)

    teacher_id = db.Column(db.Integer,
                          db.ForeignKey('teachers.teacher_id'),
                          nullable=False)
                
    
    name = db.Column(db.String(100))
    

    # bookmarked_by -> list of User objects who bookmarked this class


    dancestyles = db.relationship('DanceStyle',
                                  backref='Class')

    school = db.relationship('School',
                             backref = 'Class')



    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"""<Class 
        class_id: {self.class_id} 
        dance_id: {self.dance_id}
        school_id: {self.school_id} 
        teacher_id: {self.teacher_id}
        name: {self.name}>\n"""

       

class School(db.Model):
    """Data model for School."""

    __tablename__ = 'schools'

    school_id = db.Column(db.Integer,
                       autoincrement=True,
                       primary_key=True)

    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=True)

    teachers = db.relationship('Teacher',
                               secondary = 'teacher_schools',
                               backref = 'schools')


    

    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"""
        <School 
        school_id : {self.school_id}
        name: {self.name}
        address: {self.address}>\n"""
  



class Teacher(db.Model):
    """Data model for Teacher."""

    __tablename__ = 'teachers'

    teacher_id = db.Column(db.Integer,
                       autoincrement=True,
                       primary_key=True)
    teacher_name = db.Column(db.String(50), nullable=False)

    classes = db.relationship('Class',
                              backref = 'teachers')

    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"""
        <Teacher 
        teacher_id={self.teacher_id} 
        teacher_name={self.teacher_name}>\n"""


class TeacherSchool(db.Model):
    """Data model for TeacherSchool."""

    __tablename__ = 'teacher_schools'

    teacher_school_id = db.Column(db.Integer,
                       autoincrement=True,
                       primary_key=True)

    teacher_id = db.Column(db.Integer, 
                          db.ForeignKey('teachers.teacher_id'), 
                          nullable=False)
    school_id = db.Column(db.Integer, 
                               db.ForeignKey('schools.school_id'),             nullable=False)


    

    def __repr__(self):
        """Provide helpful representation when printed."""

        return f"""
        <TeacherSchool 
        teacher_school_id: {self.teacher_school_id} 
        teacher_id: {self.teacher_id} 
        school_id: {self.school_id}>\n"""




#########################

# class TeacherClass(db.Model):
#     """Data model for TeacherClass."""

#     __tablename__ = 'teacher_classes'

#     teacher_class_id = db.Column(db.Integer,
#                        autoincrement=True,
#                        primary_key=True)

#     teacher_id = db.Column(db.Integer, 
#                            db.ForeignKey('teachers.teacher_id'),                             nullable=False)

#     dance_class_id = db.Column(db.Integer, 
#                                db.ForeignKey('dance_classes.dance_class_id'),  nullable=False)


#     def __repr__(self):
#         """Provide helpful representation when printed."""

#         return f"""
#         <TeacherClass teacher_class_id={self.teacher_class_id} 
#         teacher_id={self.teacher_id} 
#         dance_class_id={self.dance_class_id}>"""

    



################################################################################################
def connect_to_db(app):
    """Connect the database to the Flask app."""

    # Configure to use our database.
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgres:///dance_classes"
    app.config["SQLALCHEMY_ECHO"] = False
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)




if __name__ == "__main__":
    from server import app
    connect_to_db(app)
