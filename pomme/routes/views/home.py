from flask import Blueprint
from flask import render_template

home_bp = Blueprint("home", __name__)


@home_bp.route("/", methods=["GET"])
def home_view():
    return render_template("home.html")


@home_bp.route("/metrics", methods=["GET"])
def metrics_view():
    return render_template("metrics.html")


@home_bp.route("/search", methods=["GET"])
def search_view():
    return render_template("search.html")


@home_bp.route("/crawl", methods=["GET"])
def crawl_view():
    return render_template("crawl.html")
