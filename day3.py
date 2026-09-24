#Day 3 Python Flask

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/cats", methods=["POST"])
def cats():
    name = request.form.get("name")
    return f"<h1>How are you {name}!</h1>"

#using render_template() for laoding profile.html
@app.route("/profile")
def profile():
    name = "Renan C. Sumbad Jr."
    course = "BSIT WMT"
    year = "2nd Year"
    return render_template("profile.html", name=name, course=course, year=year)

@app.route("/dashboard")
def dashboard():
    name = "Renan C. Sumbad"
    course = "BSIT 201 WM"
    year = "3rd Year"
    subjects = ["OOP", "Database", "HCI"]

    return render_template("dashboard.html", name=name, course=course, year=year, subjects=subjects )


app.run(debug=True)