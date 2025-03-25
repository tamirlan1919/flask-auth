from flask import Blueprint, request, flash, render_template
from flask_login import login_required, current_user
from app.database.engine import db

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/', methods = ['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        current_user.username = request.form.get('username')
        current_user.email = request.form.get('email')
        db.session.commit()
        flash('Ваш профиль изменен!')

    return render_template('profile.html', user = current_user)