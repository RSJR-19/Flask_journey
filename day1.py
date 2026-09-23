#DAY ONE LEARNING FLASK
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to Algrthm's Flask app"

@app.route("/about")
def about():
    return "I am studying how to use Flask\nI am 2nd year BSIT Student"

@app.route("/student/<name>")
def student(name):
    return f"Hello, {name}!"

@app.route("/course/<course_name>")
def course(course_name):
    return f"You are studying {course_name}."

@app.route("/product/<product_name>")
def product(product_name):
    return f"Product: {product_name}"

@app.route("/greet/<name>/<language>")
def greet(name, language):
    return f"{'Hello' if language == 'English' else 'Hola'}, {name}!"

#What i learned: Per each variable in <> there must be a same parameter used in the function as other wise it wont work/ throew error

app.run(debug=True)

#SUCCESS DAY 1