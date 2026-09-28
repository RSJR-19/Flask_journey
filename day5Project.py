from flask import Flask, jsonify, request, render_template
import mysql.connector


app = Flask(__name__)

connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="123renan456",
    database="pet_vet"
)

cursor = connection.cursor()

@app.route('/pets_register', methods=['GET', 'POST'])
def pet_register():
    if request.method == 'POST':
        name = request.form.get("Name")
        color = request.form.get("Color")
        issue = request.form.get("Issue")
        owner = request.form.get("Owner")

        if not name or not color or not issue or not owner:
            return jsonify({'Error_Message': 'Missing details'})

        cursor.execute("INSERT INTO vet_list(name, color, issue, owner) VALUES (%s, %s, %s, %s)", (name, color, issue, owner))
        connection.commit()

        return jsonify({
            "name" : name,
            "color" : color,
            "issue" : issue,
            "owner" : owner,
            "status" : "200 Ok"
        })
    else:
        return render_template("pet_vet.html")

app.run(debug=False)

