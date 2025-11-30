from flask import Flask
from .config import Config
from .extensions import db, migrate, csrf

def create_app(config_class=None):
    app = Flask(__name__)
    cfg = config_class or Config
    app.config.from_object(cfg)

    # init extensions
    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)

    # register blueprints
    from .main import bp as main_bp
    app.register_blueprint(main_bp)
    from .api import bp as api_bp
    app.register_blueprint(api_bp, url_prefix='/api')
    from .ingest import bp as ingest_bp
    app.register_blueprint(ingest_bp, url_prefix='/ingest')

    # cli
    from .cli import register as register_cli
    register_cli(app)

    return app
