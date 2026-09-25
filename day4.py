#day 4 Flask
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    name = "Renan"
    return render_template("home.html", name=name)

@app.route("/student", methods=['GET','POST'])
def student():

    if request.method == "POST":
        name = request.form.get("name")
        course = request.form.get("course")

        if not name or not course:
            return "Please provide both name and course"

        return f"Student: {name} || Course: {course}"

    return render_template("student.html")

@app.route("/api/student")
def api_student():
    student = {
        "name" : "Renan C. Sumbad Jr.",
        "course": "BSIT 201 WM",
        "cats": 9
    }

    return jsonify(student)
#jsonify turns dict into json
#json is used for APIs

@app.route("/cats", methods=['GET','POST'])
def cats():
    name = request.form.get("name")
    age = request.form.get("age")
    color = request.form.get("color")

    if request.method == "POST":
        if not name or not age or not color:
            return jsonify({"error": "Missing needed Infos"})

        return jsonify({
            "name": name,
            "age": int(age),
            "color": color
        })

    return render_template("cats.html")




app.run(debug=True)