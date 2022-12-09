from flask import Flask, render_template, abort

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

slug_to_project = {project["slug"]: project for project in projects}


@app.route("/")
def home():
    return render_template("home.html", projects=projects)


@app.route("/spark-notes")
def spark_notes():
    return render_template("spark_notes.html")


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/this-website")
def this_website():
    return render_template("this_website.html")


@app.route("/project/<string:slug>")
def project(slug):
    if slug not in slug_to_project:
        abort(404)
    return render_template(f"project_{slug}.html", project=slug_to_project[slug])