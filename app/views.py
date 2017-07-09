import os
from random import sample, choice, shuffle

from flask import render_template, flash, redirect, session, url_for, request, Response
#~ from flask_login import login_required, login_user, logout_user

from config import MUSICDIR
from .forms import SongForm, LoginForm
from .models import Songs#, User
from app import app, db, models


def get_choices_from_db():
    """Takes no arguments. Returns a list of the paths of 4 randomly selected songs from the Songs table."""
    choicelist_db = Songs.query.all()
    choicelist_path = []
    for x in choicelist_db:
        choicelist_path.append(x.path_with_space)
    choices = sample(choicelist_path, 4)
    return choices


def easy_to_read_name(songpath):
    """Takes a path to a song and returns just the file name without the extension."""
    list_after_split = songpath.split('/')
    songname_with_ext = list_after_split[-1]
    songname_split = os.path.splitext(songname_with_ext)
    return songname_split[0]


@app.route('/', methods=('get', 'post'))
#@login_required
def index():
    """Called with no arguments when the root URL is fetched.
    First builds correct and wrong counters if they do not exist. 
    Then calls get_choices_from_db and designates 1 song as correct and the other 3 as wrong.
    Calls easy_to_read_name and shuffles the songs before feeding to the form.
    If the form is valid on submit, checks the form value.
    If the correct answer was chosen, update the correct counter and call correct.
    If the wrong answer was chosen, update the wrong counter and call wrong.
    Returns the rendered HTML of the index.html file.
    """
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


#~ @app.route("/login/", methods=["GET", "POST"])
#~ def login():
    #~ loginform = LoginForm()
    #~ print loginform.username.data
    #~ if loginform.validate_on_submit():
        #~ username = loginform.username.data
        #~ password = loginform.password.data       
        #~ if User.query(username == username).exists() and User.query(password == password).exists():
            #~ user = User.query(username == username and password == password).first()
            #~ login_user(user)
            #~ return redirect(url_for('index'))
    #~ return render_template('login.html',
                        #~ loginform=loginform)


#~ @login_manager.user_loader
#~ def load_user(userid):
    #~ return User(userid)


#~ @app.route("/logout/")
#~ @login_required
#~ def logout():
    #~ logout_user()
    #~ return Response('<p>Logged out</p>')


@app.errorhandler(401)
def page_not_found(e):
    return Response('<p>Login failed</p>')


@app.route('/wrong/')
def wrong():
    """Called when the /wrong URL is fetched.
    Returns a rendered HTML of the wrong.html file.
    """
    correctchoice = easy_to_read_name(session['thecorrectchoice'])
    wrongcounter = session['wrongcounter']
    correctcounter = session['correctcounter']
    return render_template('wrong.html',
                        correctchoice=correctchoice,
                        wrongcounter=wrongcounter,
                        correctcounter=correctcounter)


@app.route('/correct/')
def correct():
        """Called when the /correct URL is fetched.
    Returns a rendered HTML of the correct.html file.
    """
    wrongcounter = session['wrongcounter']
    correctcounter = session['correctcounter']
    return render_template('correct.html',
                        wrongcounter=wrongcounter,
                        correctcounter=correctcounter)


@app.route('/clearscore/')
def clearscore():
    """Called when the /clearscore URL is fetched.
    Resets the correct and wrong counters and redirects to the root URL.
    """
    session['wrongcounter'] = 0
    session['correctcounter'] = 0
    return redirect('/')
