from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/beers")
def beers():
    return render_template("beers.html")


@app.route("/events")
def events():
    return render_template("events.html")


@app.route("/food")
def food():
    return render_template("food.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("home.html"), 404


if __name__ == "__main__":
    app.run(debug=True)