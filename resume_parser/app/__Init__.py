# app/__init__.py
from flask import Flask
import os

def create_app():
    app = Flask(__name__)

    # Secret key (required for flash messaging, sessions, etc.)
    app.config['SECRET_KEY'] = 'your_secret_key_here'

    # Upload folder
    app.config['UPLOAD_FOLDER'] = os.path.join(os.getcwd(), 'app', 'uploads')
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    # from .routes import main
    # app.register_blueprint(main)

    return app
