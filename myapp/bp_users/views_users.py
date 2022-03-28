import logging
from flask import render_template, abort, flash, redirect, url_for
from myapp import db
from bp_users import bp_users
from bp_users.model_users import User
from bp_users.form_users import ProfileForm


@bp_users.route('/myprofile', methods=['GET', 'POST'])
def do_my_profile():
    form = ProfileForm()

    user = User.query.get(1)
    if user:
        if form.validate_on_submit():
            user.username = form.username.data
            user.email = form.email.data
            db.session.add(user)
            db.session.commit()

        form.username.data = user.username
        form.email.data = user.email

        return render_template('users/myprofile.html', form=form, user=user)

    abort(404)


@bp_users.route('/user', defaults={'user_id': 0}, methods=['GET', 'POST'])
@bp_users.route('/user/<int:user_id>', methods=['GET', 'POST'])
def do_user(user_id):
    form = ProfileForm()

    if user_id == 0:
        user = User()
    else:
        user = db.session.query(User).get(user_id)
        if user is None:
            flash('user does not exist')

    if user:
        if form.validate_on_submit():
            user.username = form.username.data
            user.email = form.email.data
            db.session.add(user)
            db.session.commit()

            return redirect(url_for('bp_users.do_user', user_id=user.id))

        form.username.data = user.username
        form.email.data = user.email

        return render_template('users/myprofile.html', form=form, user=user)

    abort(404)


@bp_users.route('/users')
def do_users():
    users = db.session.query(User).all()
    html = render_template('users/userlist.html', users=users)

    return html
