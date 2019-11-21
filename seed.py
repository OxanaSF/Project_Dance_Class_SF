from sqlalchemy import func
from model import User, Rating, DanceStyle, Class, School, Teacher, TeacherSchool, connect_to_db, db
from server import app
import csv
import json


# 1
def load_users():
    """Load users from users_data into database."""
    with open("data/users_data.csv", encoding="ISO-8859-1") as user:
        reader = csv.reader(user)
        for row in reader:
            # print(row[1], row[2], row[3], row[4])
            user = User(email=row[1],
                        password_hash=row[2],
                        name=row[3],
                        birth_date=row[4])

            db.session.add(user)
    # db.session.commit()

# 2


def load_schools():
    """Load schools from dance_schools_data into database."""

    with open("data/dance_schools_data.csv", encoding="ISO-8859-1") as school:
        reader = csv.reader(school)
        for row in reader:
            # print(row[0], row[1], row[2], row[3] +
            #       ", " + "San Francisco, CA", row[4])
            dance_school = School(name=row[0],
                                  address=row[3] + ", " + "San Francisco, CA",
                                  website=row[2],
                                  district=row[4],
                                  phone=row[1])
            db.session.add(dance_school)
    # db.session.commit()


# 3
def load_dance_styles():
    dance_styles = ['Hip-Hop', 'Tap Dance', 'Belly Dance', 'Ballet', 'Salsa and Latin Dance', 'Kizomba', 'Jazz Dance', 'Dance Improvisation', 'East Coast Swing', 'Ballroom Dance', 'Folk Dance', 'Contemporary', 'Modern', 'Argentine Tango','Flamenco', 'Bollywood', 'Irish Dance', 'Pole Dance', 'Lindy Hop', 'Wedding Dance', 'Brazilian', 'House Dance', ' African Haitian']

    for style in sorted(dance_styles):
        new_style = DanceStyle(name=style)
        db.session.add(new_style)

    # db.session.commit()

#4
def load_teachers_from_the_pull():
    """Load teachers teachers_schools_data into database."""
    with open("data/dance_teachers_data.csv", encoding="ISO-8859-1") as user:
        reader = csv.reader(user)
        for row in reader:
            # print(row[1], row[2], row[3], row[4])
            teacher = Teacher(teacher_id=row[0],
                              teacher_name=row[1])

            db.session.add(teacher)
    # db.session.commit()


#5 Additionally could be photo or/and bio
def load_teacher_by_name(name):
    teacher = Teacher(teacher_name=name)
    db.session.add(teacher)
    db.session.commit()


#6
def load_classes_into_shool(style, school, teacher, class_name):

    the_class = Class(name=class_name)

    style = DanceStyle.query.filter_by(name=style).one()

    teacher = Teacher.query.filter_by(teacher_name=teacher).one()

    school = School.query.filter_by(name=school).one()

    the_class.dance_id = style.dance_id
    the_class.school_id = school.school_id
    the_class.teacher_id = teacher.teacher_id

    db.session.add(the_class)
    db.session.commit()


#7 add photo to existing teacher
def load_teacher_photo(teach_id, photo_link):
    the_teacher = Teacher.query.filter_by(teacher_id=teach_id).one()
    the_teacher.photo = photo_link
    db.session.commit()

#8 add bio to existing teacher
def load_teacher_bio(teach_id, bio):
    the_teacher = Teacher.query.filter_by(teacher_id=teach_id).one()
    the_teacher.bio = bio
    db.session.commit()

#9 add schedule to existing class
def load_teacher_bio(class_id_search, insert_schedule):
    the_class = Class.query.filter_by(class_id=class_id_search).one()
    the_class.schedule = insert_schedule
    db.session.commit()
     


if __name__ == "__main__":
    from server import app
    from model import connect_to_db
    connect_to_db(app)
    db.create_all()
