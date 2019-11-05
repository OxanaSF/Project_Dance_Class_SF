from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

#################################################################################################

class User(db.Model):
    """Data model for User."""

    __tablename__ = 'users'

    """Columns and/or relationships"""

    user_id = db.Column(db.Integer,
                       autoincrement=True,
                       primary_key=True, nullable=False)
    email = db.Column(db.String(100), nullable=False)

    bookmarks = db.relationship('Bookmark')
    ratings = db.relationship('Raiting')


class Bookmark(db.Model):
    """Data model for Bookmark."""

    __tablename__ = 'bookmarks'

    bookmark_id = db.Column(db.Integer,
                       autoincrement=True,
                       primary_key=True, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    dance_class_id = db.Column(db.Integer, db.ForeignKey('dance_classes.dance_class_id'), nullable=False)


    users = db.relationship('User')
    dance_classes = db.relationship('DanceClass')



class Raiting(db.Model):
    """Data model for Raiting."""

    __tablename__ = 'raitings'

    raiting_id = db.Column(db.Integer,
                       autoincrement=True,
                       primary_key=True, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    dance_class_id = db.Column(db.Integer, db.ForeignKey('dance_classes.dance_class_id'), nullable=False)


    score = db.Column(db.Integer, nullable=False)


    users = db.relationship('User')
    dance_classes = db.relationship('DanceClass')


class DanceClass(db.Model):
    """Data model for DanceClass."""

    __tablename__ = 'dance_classes'

    dance_class_id = db.Column(db.Integer,
                       autoincrement=True,
                       primary_key=True, nullable=False)

    school_id = db.Column(db.Integer, db.ForeignKey('schools.school_id'), nullable=False)
    
    dance_name = db.Column(db.String(100))
    dance_style = db.Column(db.String(50), nullable=False)


    bookmarks = db.relationship('Bookmark')
    ratings = db.relationship('Rating')
    schools = db.relationship('School')


class School(db.Model):
    """Data model for School."""

    __tablename__ = 'schools'

    school_id = db.Column(db.Integer,
                       autoincrement=True,
                       primary_key=True, nullable=False)
    school_name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)


    dance_classes = db.relationship('DanceClass')
    teachers_schools = db.relationship('TeacherSchool')



class Teacher(db.Model):
    """Data model for Teacher."""

    __tablename__ = 'teachers'

    teacher_id = db.Column(db.Integer,
                       autoincrement=True,
                       primary_key=True, nullable=False)

    
    bio = db.Column(db.String(1000))
   

    teachers_classess = db.relationship('TeacherClass')
    teachers_schools = db.relationship('TeacherSchool')


class TeacherClass(db.Model):
    """Data model for TeacherClass."""

    __tablename__ = 'teacher_classes'

    teacher_class_id = db.Column(db.Integer,
                       autoincrement=True,
                       primary_key=True, nullable=False)

    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.teacher_id'), nullable=False)
    dance_class_id = db.Column(db.Integer, db.ForeignKey('dance_classes.dance_class_id'), nullable=False)


    dance_classes = db.relationship('DanceClass')
    teachers = db.relationship('Teacher')


class TeacherSchool(db.Model):
    """Data model for TeacherSchool."""

    __tablename__ = 'teacher_schools'

    teacher_school_id = db.Column(db.Integer,
                       autoincrement=True,
                       primary_key=True, nullable=False)

    teacher_id = db.Column(db.Integer, db.ForeignKey('teachers.teacher_id'), nullable=False)
    school_id = db.Column(db.Integer, db.ForeignKey('schools.school_id'), nullable=False)


    schools = db.relationship('School')
    teachers = db.relationship('Teacher')








    
                      


                        

















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
