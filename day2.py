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
@app.route("/cats", methods=['POST'])
def cats():
    name = request.form.get("name")
    return f"Hello, {name}!"

#PUT
@app.route("/student/<id>", methods=['PUT'])
def update_student(id):
    return f"Student {id} has been updated!"

#PATCH 
@app.route("/student/<id>", methods=['PATCH'])
def patch_student(id):
    return f"Student {id} has been partially updated!"

@app.route("/student/<id>", methods=['DELETE'])
def delete_student(id):
    return f"Student {id} has been deleted!"

app.run(debug=True)