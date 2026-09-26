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

pibbles = []
@app.route("/pibble", methods=['GET', 'POST'])
def pibble():
    if request.method == "POST":
        name = request.form.get("name")
        color = request.form.get("color")
        age = request.form.get("age")

        if not age or not name or not color:
            return jsonify({'error_message' : "Empty or missing fields"})

        pibble_made = {
            "name" : name,
            "color" : color,
            "age": int(age)
        }

        pibbles.append(pibble_made)

        return jsonify(pibble_made)

    return render_template("pibble.html")

@app.route('/pibbles/<int:index>')
def get_pibble(index):
    try:
        return jsonify(pibbles[int(index)])
    except:
        return jsonify({'error_detected': 'Invalid Value!'})

@app.route('/pibbles')
def get_all_pibble():
    return jsonify(pibbles)


@app.route('/pibbles/<int:index>', methods=['PUT'])
def update_pibble(index):
    new_name = request.form.get("name")
    new_age = request.form.get("age")
    new_color = request.form.get("color")

    pibbles[index]["name"] = new_name
    pibbles[index]["age"] = int(new_age)
    pibbles[index]["color"] = new_color

    return jsonify(pibbles[index])

@app.route("/pibbles/<int:index>", methods=["DELETE"])
def delete_pibble(index):
    try:
        return jsonify(pibbles.pop(index))
    except:
        return jsonify({'error_message' : 'Invalid pibble to be deleted'})


app.run(debug=True)