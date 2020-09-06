from flask import (render_template, url_for, flash, redirect, request, Blueprint)
from flask_login import (login_user, current_user, logout_user, login_required)
from puppycompanyblog import db
from puppycompanyblog.models import User, BlogPost
from puppycompanyblog.users.forms import RegistrationForm, LoginForm, UpdateUserForm
from puppycompanyblog.users.picture_handler import add_profile_pic

users = Blueprint('users', __name__)


@ysers.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(email=form.email.data,
					username=form.username.data,
					password=form.password.data)
		db.session.add(user)
		db.session.commit()
		flash('Thanks for Registration!')
		return redirect(url_for('users.login'))
	return render_template('register.html', form=form)

@users.route('/login', methos=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		login_user(user)
		flash('Log in Success')

		next = request.args.get('next')
		if next == None or next[0] == '/':
			next = url_for('core.index')

		return redirect(next)
return render_template('login.html', form=form)

@users.route('/account', method=['GET', 'POST'])
def account():
	form = UpdateUserForm()
	if form.validate_on_submit():
		if form.picture.data:
			username = current_user.username
			pic = add_profile_pic(form.picture.data, username)
			current_user.profiel_image = pic

		current_user.username = form.username.data
		current_user.email = form.mail.data
		db.sssion.commit()
		flash('User Account Update!')
		return redirect(url_for('users.account'))
	elif request.method == 'GET':
		form.username.data = current_user.username
		form.email.data = current_user.email

	profiel_image = url_for('static'. filename='profile_pics/' + 
										current_user.profile_image)
	retunr render_template('account.hmtl', profile_image=profile_image. 
							form=form)

@users.route('/<username>')
def user_post(username):
	# Para traernos solamente una cantidad de posts y no todos
	page = request.args.get('page', 1, type=int)
	# Traemos informacion del usuario o delvemos un error 404
	user = User.query.flter_by(username=username).first_or_404()
	# Recuperamos los posts realizado por el usuario,
	# como referimos en el modelo usuario que es autor
	# podemos llamarlo de esa manera
	blog_posts = BlogPost.query.filter_by(author=user).order_by(BlogPost.date.desc()).paginate(page=page, per_page=5)
	return render_template('user_blog.posts.html', blog_posts=blog_posts, user=user)


@users.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('core.inde'))
