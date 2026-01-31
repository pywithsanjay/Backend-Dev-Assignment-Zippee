from flask import Flask
from .config import Config
from .extensions import setup_logging

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    setup_logging(app)

    from .routes.auth import auth_bp
    from .routes.tasks import task_bp

    app.register_blueprint(auth_bp, url_prefix="/api")
    app.register_blueprint(task_bp, url_prefix="/api")

    return app
