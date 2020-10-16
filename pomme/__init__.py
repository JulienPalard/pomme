import logging
import os

from celery import Celery
from dotenv import load_dotenv
from flask import Flask


POMME_ROOT = os.path.join(os.path.dirname(__file__), "../")  # refers to repository root
dotenv_path = os.path.join(POMME_ROOT, ".env")
load_dotenv(dotenv_path)

REQUIRED_ENV_VARS = [
    "FLASK_PORT",
    "FLASK_DEBUG",
    "FLASK_HOST",
    "FLASK_SECRET_KEY",
    "CELERY_BROKER_URL",
    "CELERY_RESULT_BACKEND",
]

for item in REQUIRED_ENV_VARS:
    if item not in os.environ:
        raise EnvironmentError(
            f"{item} is not set in the server's environment or .env file. It is required."
        )

from pomme.static import FLASK_SECRET_KEY, CELERY_RESULT_BACKEND, CELERY_BROKER_URL


application = Flask(__name__)

if (
    os.getenv("FLASK_DEBUG", "false") == "true"
    or os.getenv("FLASK_DEBUG", "false") == "1"
):
    application.debug = True
else:
    application.debug = False

application.secret_key = FLASK_SECRET_KEY
application.config.update(FLASK_SECRET_KEY=FLASK_SECRET_KEY)

# Celery configuration
application.config["CELERY_BROKER_URL"] = CELERY_BROKER_URL
application.config["CELERY_RESULT_BACKEND"] = CELERY_RESULT_BACKEND

logging.debug("Initializing Celery")
# Initialize Celery
celery = Celery(application.name, broker=CELERY_BROKER_URL)
celery.conf.update(application.config)


from pomme.routes.views.home import home_bp

application.register_blueprint(home_bp)


# import tasks here to be registered by celery

import pomme.tasks  # noqa
