from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = 'database.db'
custom_instance_path = path.join(path.abspath(path.dirname(__file__)), 'instance')


def create_app():
    app = Flask(__name__, instance_path=custom_instance_path, instance_relative_config=True)
    app.config["SECRET_KEY"] = "qwertyuiop asdfghjkl zxcvbnm"
    app.config["SQLALCHEMY_DATABASE_URI"] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from .models import User, Note
    create_database(app=app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    return app

def create_database(app):
    if not path.exists('notes_website/' + DB_NAME):
        with app.app_context():
            db.create_all()
        print('Created Database!')

    