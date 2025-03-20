from flask import Flask
from app.config import Config
from app.database.engine import db
from app.routes.registration import register_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)

    with app.app_context():
        from app.database import models  # Импорт моделей, чтобы они были зарегистрированы
        db.create_all()

    app.register_blueprint(register_bp, prefix_url = '/register')

    return app