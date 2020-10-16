from flask import Blueprint
from flask import flash
from flask import redirect
from flask import render_template
from flask import url_for

from pomme.forms.search import SearchForm

home_bp = Blueprint("home", __name__)


@home_bp.route("/", methods=["GET"])
def home_view():
    return render_template("home.html")


@home_bp.route("/metrics", methods=["GET"])
def metrics_view():
    return render_template("metrics.html")


@home_bp.route("/search", methods=["GET", "POST"])
def search_view():
    form = SearchForm()
    if form.validate_on_submit():
        search_word = form.search_word.data
        flash(search_word, "success")
        return redirect(url_for("home.search_view"))
    return render_template("search.html", form=form)


@home_bp.route("/crawl", methods=["GET"])
def crawl_view():
    return render_template("crawl.html")
