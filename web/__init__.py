from flask import Flask,send_from_directory
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_migrate import Migrate
from flask_login import LoginManager
import os


db = SQLAlchemy()
migrate = Migrate()
DB_name = 'database.db'
def create_app():
    app = Flask(__name__,static_folder='static',)
    
    app.config['SECRET_KEY'] = 'yANUs1 ai project'
    app.config['WTF_CSRF_ENABLED'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_name}'
    db.init_app(app)
    migrate = Migrate(app,db)
    migrate.init_app(app,db)
    
    from .views import views
    from .auth import auth
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    from .models import User,Note
    create_database(app)
    
    # flask-login 적용
    login_manager = LoginManager()
    login_manager.login_view = 'auth.sign_in'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(id)  # primary_key
    def format_datetime(value, format='%Y-%m-%d %H:%M'):
        return value.strftime(format)

    app.jinja_env.filters['datetime'] = format_datetime   
    return app



def create_database(app):
    # db파일이 확인안될 때만 생성
    if not path.exists('website/' + DB_name):
        with app.app_context():
            db.create_all()
        print('>>> Create DB')