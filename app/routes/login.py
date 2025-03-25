from flask import Blueprint, request, flash, redirect, url_for, render_template
from app.forms import LoginForm
from app.database.models import User
from app.database.engine import db
from werkzeug.security import generate_password_hash
from flask_login import login_user

login_bp = Blueprint('login', __name__)

@login_bp.route('/', methods = ['GET', 'POST'])
def sign_in():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user=user, remember=form.remember.data)
            flash('Вы вошли в систему!')
            return redirect('/profile')
        
    return render_template('login.html', form=form)
