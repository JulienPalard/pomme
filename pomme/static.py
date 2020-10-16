import os


FLASK_PORT = os.getenv("FLASK_PORT")
FLASK_DEBUG = os.getenv("FLASK_DEBUG")
FLASK_HOST = os.getenv("FLASK_HOST")
FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY")

CELERY_BROKER_URL = os.getenv("CELERY_BROKER_URL")
CELERY_RESULT_BACKEND = os.getenv("CELERY_RESULT_BACKEND")

GH_TOKEN = os.getenv("GH_TOKEN")

POMME_ROOT = os.path.join(os.path.dirname(__file__), "../")  # refers to repository root
