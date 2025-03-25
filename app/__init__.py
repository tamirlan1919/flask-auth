from flask import Flask
from app.config import Config
from app.database.engine import db
from app.routes.registration import register_bp
from app.routes.login import login_bp
from app.routes.profile import profile_bp

from flask_login import LoginManager
from app.database.models import User

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        from app.database import models  # Импорт моделей, чтобы они были зарегистрированы
        db.create_all()

    # Инициализация LoginManager
    login_manager = LoginManager()
    login_manager.login_view = 'login.sign_in'  # укажи имя функции входа
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    app.register_blueprint(register_bp, url_prefix = '/register')
    app.register_blueprint(login_bp, url_prefix = '/login')
    app.register_blueprint(profile_bp, url_prefix = '/profile')

    return app