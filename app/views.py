from app import app
from .forms import LoginForm
from flask import render_template, flash, redirect

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Rob'} # fake user
	items = [
		{
			'owner': {'nickname': 'Bill'},
			'location': '3rd Street Pub',
			'description': 'Black Northface Jacket'

		},
		{
			'owner': {'nickname': 'Nicole'},
			'location': '20th and Park',
			'description': 'iPhone 6'
		}
	]
	return render_template('index.html',
							title='Home',
							user=user,
							items=items)

@app.route('/login', methods=['GET', 'POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		flash('Login requested for OpenID="%s", remember_me=%s' \
			% (form.openid.data, str(form.remember_me.data)))
		return redirect('/index')
	return render_template('login.html',
							title='Sign In',
							form=form,
							providers=app.config['OPENID_PROVIDERS'])