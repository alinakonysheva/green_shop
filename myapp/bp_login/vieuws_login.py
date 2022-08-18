from myapp import db,create_app as myapp
from flask import render_template,flash, redirect, url_for, request
from myapp.bp_login.form_login import LoginForm,RegistrationForm
from flask_login import current_user, login_user, login_required,logout_user
from werkzeug.urls import url_parse
from myapp.bp_login import bp_login
from myapp.bp_users.model_users import User




@bp_login.route('/')
@bp_login.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('bp_user.do_my_profile', user_id=current_user.id))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('bp_login.login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('bp_general.home')
        return redirect(next_page)
    return render_template('login.html', title='Sign In', form=form)

@bp_login.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('bp_login.login'))

@bp_login.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('bp_general.home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(firstname=form.firstname.data, lastname=form.lastname.data,email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('bp_login.login'))
    return render_template('register.html', title='Register', form=form)