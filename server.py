from flask import Flask, render_template, request, flash, redirect, session, jsonify

from flask_debugtoolbar import DebugToolbarExtension

from jinja2 import StrictUndefined

from model import connect_to_db, db, User, Bookmark, Rating, DanceStyle, Class, School, Teacher, TeacherSchool

from query_test import find_classes_by_dance_style
from datetime import date, datetime, timezone



app = Flask(__name__)

app.secret_key = "ABC"

app.jinja_env.undefined = StrictUndefined

# route 1
@app.route('/')
def homepage():
    """Displays homepage and sign-in/login info."""
    today = datetime.today().strftime("%b %d %Y")
  

    return render_template("homepage.html", today=today)


# route 2
@app.route('/register', methods=['GET'])
def register_form():
    """Show form for user signup for new user"""

    return render_template("register_form.html")


# route 3
@app.route('/register', methods=['POST'])
def register_process():
    """Process registration."""

    email = request.form.get("email")

    existing_email = User.query.filter_by(email=email).first()

    if existing_email:
        flash("this email name is not avaliable")
        return redirect("/register")
    else:
        email = request.form.get("email")
        password = request.form.get("password")
        name = request.form.get("name")
        birthday = request.form.get("birthday")

        new_user = User(email=email,        password_hash=password,
                        name=name, birth_date=birthday)
        db.session.add(new_user)
        db.session.commit()

        flash(f"User {name} added.")

        return redirect(f"/users/{new_user.user_id}")


# route 4
@app.route('/login', methods=['GET'])
def login_form():
    """Show login form."""

    return render_template("login_form.html")


# route 5
@app.route('/loggedin', methods=['POST'])
def login_process():
    """Process login."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = User.query.filter_by(email=email).first()
    # user = User.query.filter(User.email == email, User.password_hash == password).one()

    if not user:
        flash("Your login is invalid. Please try again.")
        return redirect("/")

    if user.password_hash != password:
        flash("Incorrect password. Please try again.")
        return redirect("/")

    session["user_id"] = user.user_id

    flash("Logged in")
    return redirect(f"/users/{user.user_id}")

# route 6
@app.route('/logout')
def logout():
    """Log out."""

    del session["user_id"]
    flash("Logged Out.")
    return redirect("/")

# route 7
@app.route("/users")
def user_list():
    """Show list of users."""

    users = User.query.all()
    return render_template("user_list.html", users=users)

# route 8
@app.route("/users/<int:user_id>")
def user_detail(user_id):
    """Show info about user."""

    user = User.query.get(user_id)
    return render_template('user.html', user=user)

# route 9
@app.route('/dance_schools')
def show_schools():
    """Shows dance styles options"""

    dance_schools = School.query.all()

    return render_template('dance_schools.html',
                           dance_schools=dance_schools)

# route 10
@app.route('/dance_school/<school_id>')
def show_school(school_id):

    dance_school = School.query.get(school_id)



    # print(dance_school.classes)
    # print(dance_school.teachers)

    return render_template('dance_school.html', dance_school=dance_school)


# route 11
@app.route('/dance_styles')
def show_dance_styles():
    """Shows dance_styles"""

    dance_styles = DanceStyle.query.all()

    return render_template('dance_styles.html',
                           dance_styles=dance_styles)

# route 12
@app.route('/dance_style/<dance_id>')
def show_classes_based_on_style(dance_id):

    dance_style = DanceStyle.query.get(dance_id)

    dance_classes = dance_style.dancestyle

    # teachers = []
    # for class_ in dance_classes:
    #     teachers.append(class_.teacher)
    # print(teachers)

    return render_template('dance_style.html', dance_style=dance_style, dance_classes=dance_classes
                           )


# route 13
@app.route('/dance_classes')
def show_dance_classes():
    """Shows dance classes"""

    dance_classes = Class.query.all()

    return render_template('dance_classes.html',
                           dance_classes=dance_classes)


# route 14
@app.route('/dance_class/<class_id>')
def show_particular_class(class_id):

    dance_class = Class.query.get(class_id)

    # dance_school = dance_school.school

    # dance_teacher = dance_school.classes

    return render_template('dance_class.html', dance_class=dance_class)



# route 15
@app.route('/dance_teachers')
def show_dance_teachers():
    """Shows dance teachers"""

    dance_teachers = Teacher.query.all()

    return render_template('dance_teachers.html',
                           dance_teachers=dance_teachers)

# route 16
@app.route("/dance_teachers/<int:teacher_id>", methods=['GET'])
def show_teacher_info(teacher_id):
    """Show info about teacher. If a user is logged in, let them add/edit a rating.
    """

    teacher = Teacher.query.get(teacher_id)

    dance_classes = teacher.classes

    user_id = session.get("user_id")

    if user_id:
        user_rating = Rating.query.filter_by(teacher_id=teacher_id, 
                                            user_id=user_id).first()
    else:
        user_rating = None


    return render_template('dance_teacher.html', teacher=teacher,                                             dance_classes=dance_classes, user_rating=user_rating)

# route 17
@app.route("/dance_teachers/<int:teacher_id>", methods=['POST'])
def teacher_detail_process(teacher_id):
    """Add/edit a rating."""

    score = int(request.form["score"])
    user_id = session.get("user_id")
    if not user_id:
        raise Exception("No user logged in.")

    rating = Rating.query.filter_by(user_id=user_id, teacher_id=teacher_id).first()

    if rating:
        rating.score = score
        flash("Rating updated.")

    else:
        rating = Rating(user_id=user_id, teacher_id=teacher_id, score=score)
        flash("Rating added.")
        db.session.add(rating)

    db.session.commit()

    return redirect(f"/dance_teachers/{teacher_id}")



if __name__ == "__main__":
    # We have to set debug=True here, since it has to be True at the point
    # that we invoke the DebugToolbarExtension

    # Do not debug for demo
    app.debug = True
    app.cache = False

    connect_to_db(app)

    # Use the DebugToolbar
    # DebugToolbarExtension(app)

    app.run(host="0.0.0.0")
