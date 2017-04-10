from flask import render_template, flash, redirect, session, url_for, request
from app import app, db, models
from random import sample, choice, shuffle
from .forms import SongForm
import os
from .models import Songs
from config import musicdir

def getchoicesfromdb():
	choicelist_db = Songs.query.all()
	choicelist_path = []
	for x in choicelist_db:
		choicelist_path.append(x.path_with_space)
	choices = sample(choicelist_path, 4)
	return choices

def easytoreadname(songpath):
	listaftersplit = songpath.split('/')
	songname_with_ext = listaftersplit[-1]
	songname_split = os.path.splitext(songname_with_ext)
	return songname_split[0]
						
@app.route('/', methods=('get', 'post'))
def index():
	try:
		if session['wrongcounter'] != 0 or session['correctcounter'] != 0:
			pass
	except:
		session['wrongcounter']=0
		session['correctcounter']=0
	form = SongForm()
	allchoices = getchoicesfromdb()
	wrongchoices = allchoices[1:4]
	correctchoice = allchoices[0]
	formchoices = []
	for i, name in enumerate(allchoices):
		formchoices.append((i, easytoreadname(name)))
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
						musicdir=musicdir,
						wrongcounter=wrongcounter,
						correctcounter=correctcounter)

@app.route('/wrong')
def wrong():
	correctchoice = easytoreadname(session['thecorrectchoice'])
	wrongcounter = session['wrongcounter']
	correctcounter = session['correctcounter']
	return render_template('wrong.html',
						correctchoice=correctchoice,
						wrongcounter=wrongcounter,
						correctcounter=correctcounter)
	
@app.route('/correct')
def correct():
	wrongcounter=session['wrongcounter']
	correctcounter=session['correctcounter']
	return render_template('correct.html',
						wrongcounter=wrongcounter,
						correctcounter=correctcounter)
						
@app.route('/clearscore')
def clearscore():
	session['wrongcounter'] = 0
	session['correctcounter'] = 0
	return redirect('/')
