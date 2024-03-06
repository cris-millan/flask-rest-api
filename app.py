import os

from datetime import timedelta

from flask import Flask
from flask_migrate import Migrate
from flask_smorest import Api

from src.config import TOKEN_CONFIG
from src.data.postgres.db import db
from extensions import jwt
from seeds.seed import register_commands
from src.drivers import CacheDriverFactory

from src.routes.users import blue_print as user_bp
from src.routes.auth import blue_print as auth_bp
from src.routes.cache import blue_print as cache_bp


# import logging


def create_app(db_url=None):
    app = Flask(__name__)

    # logging.basicConfig(filename='record.log', level=logging.DEBUG,
    #                     format=f'%(asctime)s %(levelname)s %(name)s %(threadName)s: %(message)s')

    app.config["PROPAGATE_EXCEPTIONS"] = True
    app.config["API_TITLE"] = "Millan App"
    app.config["API_VERSION"] = "v1"
    app.config["OPENAPI_VERSION"] = "3.0.3"
    app.config["OPENAPI_URL_PREFIX"] = "/"
    # app.config["OPENAPI_SWEAGER_UI_PATH"] = "/sweager-ui"
    # app.config["OPENAPI_SWEAGER_UI_URL"] =
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url or os.getenv("DATABASE_URL", "sqlite:///data2.db")
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
    app.config["SQLALCHEMY_TRACK_NOTIFICATIONS"] = False

    db.init_app(app)
    migrate = Migrate(app, db)

    # Initialize seeders commands
    register_commands(app, db)

    # with app.app_context():
    #     db.create_all()

    api = Api(app)

    app.config["JWT_SECRET_KEY"] = "Millan@"
    app.config["JWT_ACCESS_TOKEN_EXPIRES"] = timedelta(minutes=TOKEN_CONFIG["token_live"])
    app.config["JWT_REFRESH_TOKEN_EXPIRES"] = timedelta(minutes=TOKEN_CONFIG["fresh_token_live"])

    # initialize jwt
    jwt.init_app(app)

    # Blueprints register

    api.register_blueprint(user_bp)
    api.register_blueprint(auth_bp)
    api.register_blueprint(cache_bp)



    # app.logger.info('Info level log')

    if __name__ == '__main__':
        app.run(debug=True)

    return app
