from flask import Blueprint
from flask import render_template

home_bp = Blueprint("home", __name__)


@home_bp.route("/", methods=["GET"])
def home_view():
    return render_template("metrics.html")
