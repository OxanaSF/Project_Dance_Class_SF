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
    db.session.commit()


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
    db.session.commit()


# 3
def load_dance_styles_photos():
    with open("data/dance_styles_data.csv", encoding="ISO-8859-1") as style:
        reader = csv.reader(style)
        for row in reader:
            # print(row[1], row[2], row[3], row[4])
            style = DanceStyle(photo=row[1],
                               name=row[2])

            db.session.add(style)
    db.session.commit()


# 4
def load_teachers_from_the_pull():
    """Load teachers into database."""
    with open("data/dance_teachers_data.csv", encoding="ISO-8859-1") as teach:
        reader = csv.reader(teach)
        for row in reader:
            # print(row[])
            teacher = Teacher(photo=row[1], teacher_name=row[3], bio=row[4])

            db.session.add(teacher)
    db.session.commit()


# 5
def load_schools_dance_styles_teachers():
    schools = load_schools()
    styles = load_dance_styles_photos()
    teachers = load_teachers_from_the_pull()
    # classes = load_classes_from_the_pull()
    return schools, styles, teachers


# 6 
def load_classes_from_the_pull():
    """Load classes into database."""
    with open("data/dance_classes_data.csv", encoding="ISO-8859-1") as dance_cl:
        reader = csv.reader(dance_cl)
        for row in reader:
            print(row[0], row[1], row[2], row[3],row[4], 'abcde' )
            dance_class = Class(dance_id=row[0], 
                                school_id=row[1], 
                                teacher_id=row[2],
                                name=row[3], 
                                schedule=row[4])

            db.session.add(dance_class)
    db.session.commit()



# 7 
def load_teacher_by_name(name, bio, photo):

    teacher = Teacher(teacher_name=name, bio=bio, photo=photo)
    db.session.add(teacher)
    db.session.commit()


#8
def load_classes_into_shool(class_name, style, school, teacher):
    the_class = Class(name=class_name)

    style = DanceStyle.query.filter_by(name=style).one()

    school = School.query.filter_by(name=school).one()

    teacher = Teacher.query.filter_by(teacher_name=teacher).one()

    

    the_class.dance_id = style.dance_id
    the_class.school_id = school.school_id
    the_class.teacher_id = teacher.teacher_id
   

    db.session.add(the_class)
    db.session.commit()


# 9 add photo to existing teacher
def load_teacher_photo(teach_id, photo_link):
    the_teacher = Teacher.query.get(teacher_id)
    the_teacher.photo = photo_link
    db.session.commit()


# 10 add bio to existing teacher


def load_teacher_bio(teacher_id, bio):
    the_teacher = Teacher.query.get(teacher_id)
    the_teacher.bio = bio
    db.session.commit()


# 11 add schedule to existing class


def load_class_schedule(class_id_search, insert_schedule):
    the_class = Class.query.get(class_id)
    the_class.schedule = insert_schedule
    db.session.commit()





if __name__ == "__main__":
    from server import app
    from model import connect_to_db
    connect_to_db(app)
    db.create_all()
