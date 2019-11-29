from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import InputTextForm, SearchForm
import TapSearch as ts


@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", title="Home")


@app.route("/input_text", methods=["GET", "POST"])
def input_text():
    form = InputTextForm()
    if form.validate_on_submit():
        print(form.text_in.raw_data)
        indexed = ts.processing(form.text_in.raw_data)
        if indexed:
            flash("Correctly indexed into database")
        return redirect(url_for("index"))
    return render_template("input_text.html", title="Input Text", form=form)


@app.route("/search", methods=["GET", "POST"])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        results = ts.searching(form.word.data, form.number_of_res.data)
        # print(results)
        return render_template("results.html", title="Results", results=results)
    return render_template("search.html", title="Search", form=form)


@app.route("/clear")
def clear():
    ts.clear()
    flash("Database flushed")
    return redirect(url_for("index"))


@app.route("/full_data")
def full_data():
    results = ts.documents
    return render_template("full_data.html", title="DATABASE", results=results)
