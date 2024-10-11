from flask import Flask
from flask_sqlachemy import SQLAlchemy
import os

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'SKFJSAFJJKkjfpojwoi32989@2094%ji9843FJHEUHJNVIU98IFWEBIIJ0WFE#S9JHI'
    app.config['IMAGE_FOLDER'] = 'ecommerce/static/images'
    app.config['SQLALCHEMY_DATABASE_URI'] = './static/images'

    app.config['SESSION_COOKIE_SECURE'] = True
    app.config['SESSION_PROTECTION'] = "strong"


    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/auth")

    with app.app_context():
        db.create_all()

    return app