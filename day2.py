#Day 2 Flask Journey 
from flask import Flask, request

#GET method 
#request.args.get()

app = Flask(__name__)

@app.route("/students")
def students():
    name = request.args.get("name")
    return f"Welcome, {name}!"

#request.args.get is for getting the search query value like in /students?name=Renan
#it gets the value of name (Renan)

#multiple search
@app.route("/profile")
def profile():
    name = request.args.get("name")
    course = request.args.get("course")
    return f"Name: {name}\nCourse: {course}"

#Post method
@app.route("/friends", methods=['POST'])
def friends():
    age = request.form.get("age")
    return f"Hello friend {age}!"

@app.route("/cats", methods=["POST"])
def cats():
    name = request.form.get("name")
    return f"Good Morning, {name}!"

app.run(debug=True)