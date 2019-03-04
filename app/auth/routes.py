from datetime import datetime

from flask import render_template, flash, redirect, url_for, request, g
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from flask_babel import _, get_locale

from app import app, db
from app.auth.forms import LoginForm, RegistrationForm, EditProfileForm, PostForm
from app.models import User, Post


@app.route('/login', methods=['POST', 'GET'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash(_("Invalid username or password!"))
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template("login.html", title="Sign In", form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/register', methods=['POST', 'GET'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(_("Congratulation! You are now registrated user!"))
        return redirect(url_for('login'))
    return render_template("register.html", title='Register', form=form)


@app.route('/reset_password_request', methods=['POST', 'GET']):
def reset_password():
    pass
