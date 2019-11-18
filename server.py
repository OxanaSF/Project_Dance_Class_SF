from flask import Flask, render_template, request, flash, redirect, session, jsonify

from flask_debugtoolbar import DebugToolbarExtension

from jinja2 import StrictUndefined

from model import connect_to_db, db, User, Bookmark, Rating, DanceStyle, Class, School, Teacher, TeacherSchool

from query_test import find_classes_by_dance_style


app = Flask(__name__)

app.secret_key = "ABC"

app.jinja_env.undefined = StrictUndefined

# route 1
@app.route('/')
def homepage():
    """Displays homepage and sign-in/login info."""

    return render_template("homepage.html")


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

        new_user = User(email=email, password_hash=password,
                        name=name, birth_date=birthday)
        db.session.add(new_user)
        db.session.commit()

        flash(f"User {email} added.")

        return redirect(f"/welcome/{new_user.user_id}")


# route 4
@app.route('/login', methods=['GET'])
def login_form():
    """login for registered users."""
    
    return render_template("login_form.html")

# route 5
@app.route('/login', methods=['POST'])
def login_process():
    """Process login."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = User.query.filter_by(email=email).first()

    if not user:
        flash("Your login is invalid. Please try again.")
        return redirect("/")

    if user.password_hash != password:
        flash("Incorrect password. Please try again.")
        return redirect("/")

    session["user_id"] = user.user_id

    flash("Logged in")
    return redirect(f"/welcome/{user.user_id}")


# route 6
@app.route("/welcome/<int:user_id>")
def user_detail(user_id):
    """Show info about user."""

    user = User.query.filter_by(user_id=user_id).first()
    return render_template('welcome.html', user=user)

# route 7
@app.route('/dance_schools')
def show_schools():
    """Shows dance styles options"""

    dance_schools = School.query.all()

    return render_template('dance_schools.html',
                           dance_schools=dance_schools)

# route 8
@app.route('/dance_school/<school_id>')
def show_school(school_id):

    dance_school = School.query.get(school_id)

    dance_class = dance_school.classes

    dance_teacher = dance_school.teachers

    # print(dance_school.classes)
    # print(dance_school.teachers)

    return render_template('dance_school.html', dance_school=dance_school, dance_class=dance_class, dance_teacher=dance_teacher)



# route 9
@app.route('/dance_styles')
def show_dance_styles():
    """Shows dance_styles"""

    dance_styles = DanceStyle.query.all()


    return render_template('dance_styles.html',
                           dance_styles=dance_styles)

# route 10
@app.route('/dance_style/<dance_id>')
def show_classes_based_on_style(dance_id):

    dance_style = DanceStyle.query.get(dance_id)

    dance_classes = dance_style.dancestyle
   

    return render_template('dance_style.html', dance_style=dance_style, dance_classes=dance_classes)
    


# route 11
@app.route('/dance_classes')
def show_dance_classes():
    """Shows dance styles options"""

    dance_classes = Class.query.all()

    return render_template('dance_classes.html',
                           dance_classes=dance_classes)


# route 12
@app.route('/dance_classes/<class_id>')
def show_particular_class(class_id):

    dance_class = Class.query.get(class_id)

    # dance_school = dance_school.school

    # dance_teacher = dance_school.classes


    return render_template('dance_class.html', dance_class=dance_class)


# route 13
@app.route('/search')
def search():
    """Dance search page."""

    # Get value from query parameter "style" from URL
    # Example query parameter with value:
    # ?<param>=<value>
    dance_style = request.args.get('dance_style')

    dance_school = request.args.get('dance_school')

    dance_teacher = request.args.get('dance_teacher')

    # from more options to less 
    if dance_style and dance_school and dance_teacher:
        result = 'a'

    elif dance_style and dance_school:
        result = 'b'


    elif dance_style and dance_teacher:
        result = 'c'


    elif dance_school and dance_teacher:
        result = 'd'


    elif dance_style:
        result = Class.query.filter(Class.name.like(f"%{dance_style}%")).all()


    elif dance_school:
        if dance_school == 'All Schools':
            result = School.query.all()
        else:
            result = School.query.filter_by(name=dance_school).all()


    elif dance_teacher:
        if dance_teacher == 'All Teachers':
            result = Teacher.query.all()
        else:
            result = Teacher.query.filter_by(teacher_name=dance_teacher).all()

   

    return render_template("search.html", results=result)


# #route 13
@app.route('/logout')
def logout():
    """Log out."""

    del session["user_id"]
    flash("Logged Out.")
    return redirect("/")


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
