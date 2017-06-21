import os
from random import sample, choice, shuffle

from flask import render_template, flash, redirect, session, url_for, request, Response
from flask_login import login_required, login_user, logout_user

from config import MUSICDIR
from .forms import SongForm, LoginForm
from .models import Songs, User
from app import app, db, models, login_manager


def get_choices_from_db():
    choicelist_db = Songs.query.all()
    choicelist_path = []
    for x in choicelist_db:
        choicelist_path.append(x.path_with_space)
    choices = sample(choicelist_path, 4)
    return choices


def easy_to_read_name(songpath):
    list_after_split = songpath.split('/')
    songname_with_ext = list_after_split[-1]
    songname_split = os.path.splitext(songname_with_ext)
    return songname_split[0]


@app.route('/', methods=('get', 'post'))
@login_required
def index():
    print "index start" 
    try:
        if session['wrongcounter'] != 0 or session['correctcounter'] != 0:
            pass
    except:
        session['wrongcounter'] = 0
        session['correctcounter'] = 0
    form = SongForm()
    allchoices = get_choices_from_db()
    wrongchoices = allchoices[1:4]
    correctchoice = allchoices[0]
    formchoices = []
    for i, name in enumerate(allchoices):
        formchoices.append((i, easy_to_read_name(name)))
    shuffle(formchoices)
    form.song_id.choices = formchoices
    if form.validate_on_submit():
        if form.song_id.data == 0:
            session['correctcounter'] = session['correctcounter'] + 1
            return redirect(url_for('correct'))
        else:
            session['wrongcounter'] = session['wrongcounter'] + 1
            return redirect(url_for('wrong'))
    session['thecorrectchoice'] = correctchoice
    correctcounter = session['correctcounter']
    wrongcounter = session['wrongcounter']
    return render_template('index.html', 
                        title='Guess That Song', 
                        form=form, 
                        correctchoice=correctchoice, 
                        wrongchoices=wrongchoices, 
                        musicdir=MUSICDIR,
                        wrongcounter=wrongcounter,
                        correctcounter=correctcounter)


#NEED TO FIX LOGIN HERE. COORDINATE WITH DATABASE AND LOGIN FORM
@app.route("/login/", methods=["GET", "POST"])
def login():
    loginform = LoginForm()
    print loginform.username.data
    if loginform.validate_on_submit():
        username = loginform.username.data
        password = loginform.password.data       
        if User.query(username == username).exists() and User.query(password == password).exists():
            user = User.query(username == username and password == password).first()
            login_user(user)
            #~ return redirect(request.args.get('next'))
            return redirect(url_for('index'))
        #~ else:
            #~ return abort(401)
    return render_template('login.html',
                        loginform=loginform)


@login_manager.user_loader
def load_user(userid):
    #~ return User.query.get(int(id))
    return User(userid)


@app.route("/logout/")
@login_required
def logout():
    logout_user()
    return Response('<p>Logged out</p>')


@app.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login failed</p>')


@app.route('/wrong/')
def wrong():
    correctchoice = easy_to_read_name(session['thecorrectchoice'])
    wrongcounter = session['wrongcounter']
    correctcounter = session['correctcounter']
    return render_template('wrong.html',
                        correctchoice=correctchoice,
                        wrongcounter=wrongcounter,
                        correctcounter=correctcounter)


@app.route('/correct/')
def correct():
    wrongcounter = session['wrongcounter']
    correctcounter = session['correctcounter']
    return render_template('correct.html',
                        wrongcounter=wrongcounter,
                        correctcounter=correctcounter)


@app.route('/clearscore/')
def clearscore():
    session['wrongcounter'] = 0
    session['correctcounter'] = 0
    return redirect('/')
