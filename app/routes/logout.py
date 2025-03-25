from flask import Blueprint, flash, redirect
from flask_login import login_required, logout_user

logout_bp = Blueprint('logout', __name__)

@logout_bp.route('/')
@login_required
def log_out():
    logout_user()
    flash('Вы вышли из аккаута')
    return redirect('/login')
    
