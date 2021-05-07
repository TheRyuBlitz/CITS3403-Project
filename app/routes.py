from flask import render_template, url_for, redirect, flash
from app import app, db
from app.forms import LoginForm, RegistrationForm
from flask_login import current_user, login_user, logout_user
from app.models import User, Quiz, Topic
from flask_login import login_required
#Place @login_required for pages that require users to be signed in

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    return render_template('Home.html', title='Home')

@app.errorhandler(404)
def error404(e):
    return render_template('404.html', title='error 404')

@app.route('/lesson')
@login_required
def content():
    return render_template('Content.html', title='Learn')


@app.route('/feedback')
@login_required
def feedback():
    return render_template('Feedback.html', title='Feedback')


@app.route('/statistics')
def statistics():
    return render_template('Statistics.html', title='Statistics')


@app.route('/lesson/<int:id>')
@login_required
def lesson(id):
    lesson = Topic.query.filter_by(id=id).first()
    if lesson == None: return 'Not Found'
    # return f"TODO + {lesson.topiccontent}"
    return render_template('Lesson.html', title='Lesson', lesson=lesson)

@app.route('/assessment')
@login_required
def assessmentHome():
    return "Assessment Home Page"
    
@app.route('/assessment/<int:quizId>')
def assessment(quizId):
    # There must be a variable that defines which topic this quiz will cover
    quiz = Quiz.query.filter_by(id=quizId).first()
    if quiz == None: return 'Not Found'
    return render_template('Assesment.html', title='Assessment', quiz=quiz)


#Login/Registration
@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated: return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.username.data).first()
        if user == None or not user.check_password(form.password.data): return "Invalid Login"
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('index'))
    return render_template('Login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('login'))
    return render_template('Registration.html', title='Registration', form=form)

