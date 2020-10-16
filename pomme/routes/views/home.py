from flask import Blueprint
from flask import flash
from flask import render_template

from pomme.forms.search import SearchForm
from pomme.models.entry import Entry

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
        word = form.search_word.data
        search_results = Entry.search(word)
        count = search_results.count()
        result_list = []
        for result in search_results:
            result_list.append(
                {"rowid": result.rowid, "msgid": result.msgid, "msgstr": result.msgstr}
            )
        flash(f"Found {count} results for '{word}'", "success")
        return render_template(
            "search.html", form=form, results=result_list, search_word=word
        )
    return render_template("search.html", form=form, results=None)


@home_bp.route("/crawl", methods=["GET"])
def crawl_view():
    return render_template("crawl.html")
