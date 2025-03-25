from flask import Blueprint, flash, redirect, render_template
from app.forms import RegistrationForm
from app.database.models import User
from app.database.engine import db
from werkzeug.security import generate_password_hash


register_bp = Blueprint('registration', __name__)

@register_bp.route('/', methods = ['POST', 'GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
         
        hashed_password = generate_password_hash(form.password.data)
        user = User(username = form.username.data, email = form.email.data,
                    password_hash = hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Регистрация успешна! Теперь войдите в систему.', 'success')
        return redirect('/')
    
    return render_template('register.html', form = form)

    





