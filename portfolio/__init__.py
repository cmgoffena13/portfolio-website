from flask import Flask, render_template

app = Flask(__name__)

projects = [
    {
        "name": "test project name",
        "thumb": "",
        "hero": "",
        "categories": ["python", "web"],
        "slug": "habit-tracking",
        "prod": ""
    }
]


@app.route("/")
def home():
    return render_template("home.html", projects=projects)


@app.route("/spark")
def spark():
    return render_template("spark.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/this-website")
def this_website():
    return render_template("this_website.html")
