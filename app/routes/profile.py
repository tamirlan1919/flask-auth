from flask import Blueprint, request, flash, redirect, url_for, render_template
from app.forms import RegistrationForm
from app.database.models import User
from app.database.engine import db
from werkzeug.security import generate_password_hash
from flask_login import login_required, current_user

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/')
@login_required
def profile():
    return f'Привет {current_user.username}'