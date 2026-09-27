#Day 4 Project - Making a LMS Student Signup
from flask import Flask, request, render_template, jsonify

app = Flask(__name__)
students = []


@app.route('/student_signup', methods=['GET', 'POST'])
def signup_students():
    if request.method == 'POST':
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        course = request.form.get("course")
        year = request.form.get("year")

        if not name or not email or not password or not course or not year:
            return jsonify({'Error_message' : 'Details Cannot be Empty'})

        for student in students:
            if email == student['email']:
                return jsonify({'Error_message': 'Only Unique Email values acceptable'})

        student = {
            "name" : name,
            "email" : email,
            "password" : password, #encrypt this,
            "course" : course,
            "year" : int(year)
        }

        students.append(student)

        return jsonify(student)

    return render_template("studentLMS.html")

@app.route("/students")
def display_students():
    return jsonify(students)

@app.route("/students/<int:index>")
def display_one_student(index):
    try:
        return jsonify(students[index])
    except:
        return jsonify({'Error_message' : 'Student Not Found'})


app.run(debug=True)