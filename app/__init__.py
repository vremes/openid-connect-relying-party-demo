from dotenv import load_dotenv, dotenv_values
from flask import Flask
from flask_oidc import OpenIDConnect

oidc = OpenIDConnect()

def create_app() -> Flask:
    """Flask application factory."""
    app = Flask(__name__)

    load_dotenv()

    app.config.from_mapping(dotenv_values())

    oidc.init_app(app)

    from app.blueprints.main import main_bp
    
    app.register_blueprint(main_bp)

    return app
