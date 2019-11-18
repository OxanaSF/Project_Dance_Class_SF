

from model import db, User, Bookmark, Rating, DanceStyle, Class, School, Teacher, TeacherSchool



def dance_style_dance_school_dance_teacher():
    """returns """


def classes_school():
    """Returns class and school where the class it tought"""
    class_school = db.session.query(Class.name,
                                    School.name).join(School).all()
    return class_school


def teachers_schools():
    """Returns name of a school and name of a tacher who teaches at the school"""
    class_school = db.session.query(TeacherSchool.teacher_school_id,
                                    School.name, Teacher.teacher_name).join(School).join(Teacher).all()
    
    return class_school


def find_classes_by_dance_style(dance_style):
    """takes in a dance style as a parameter and returns a list of all of Class objects which have that dance style."""

    list_of_classes_by_style = (db.session.query(Class).join(DanceStyle).filter(DanceStyle.name == dance_style).all())
  

    return list_of_classes_by_style


def find_classes_by_teacher_name(teacher_name):
    """takes in a teacher's name as a parameter and returns a list of all of Class objects which have teacher with that name."""

    list_of_classes_by_teacher = (db.session.query(Class).join(Teacher).filter(Teacher.teacher_name == teacher_name).all())

  
    return list_of_classes_by_teacher


def find_classes_by_school(school_name):
    """takes in school name and returns a list of all of Class objects which have that name."""

    list_of_classes_by_school = (db.session.query(Class).join(School).filter(School.name == school_name).all())

  
    return list_of_classes_by_school


def print_classes_by_dance_style(dance_style):
    """takes dance style as a parameter and returns the name of the style with the list of classes of that style"""

    classes_result = (db.session.query(Class).join(DanceStyle).filter(DanceStyle.name == dance_style).all())
    display_dict = {}

    for class_el in classes_result:
        dance_style = class_el.dancestyle.name
        dance_class = class_el.name
    
       

        display_dict[f'{dance_style}'] = display_dict.get(f'{dance_style}', [])
        display_dict[f'{dance_style}'].append(f'{dance_class}')


    return display_dict

   
def classes_by_dance_style_with_school(dance_style):
    classes_result = (db.session.query(Class).join(DanceStyle).join(School).filter(DanceStyle.name == dance_style).all())
    return classes_result

def print_classes_by_dance_style_with_school(dance_style):
    """takes dance style as a parameter and returns the name of the style with the list of classes of that style and the name of the school where the class id thought"""


    classes_result = (db.session.query(Class).join(DanceStyle).join(School).filter(DanceStyle.name == dance_style).all())
    display_dict = {}

    for class_el in classes_result:
        dance_style = class_el.dancestyle.name
        dance_class = class_el.name
        school = class_el.school.name
    

        display_dict[f'{dance_style}'] = display_dict.get(f'{dance_style}', [])
        display_dict[f'{dance_style}'].append(f'{dance_class} at {school}')
       
    return display_dict
    

def print_classes_by_dance_style_and_school(dance_style, school_name):
    """takes dance style and a school name as parameters and returns the name of the all combinations class name+school"""


    classes_result = (db.session.query(Class).join(DanceStyle).join(School).filter(DanceStyle.name == dance_style, School.name == school_name).all())


    for class_el in classes_result:
        dance_class = class_el.name
        school = class_el.school.name

  
        print(dance_class, 'class at', school)
  
   


    
  
 
    



if __name__ == "__main__":
    from server import app
    from model import connect_to_db

    connect_to_db(app)
