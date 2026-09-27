#Day 5 connecitng Flask to Mysql
from flask import Flask, render_template, jsonify, request
from dotenv import load_dotenv
import mysql.connector
import os

load_dotenv()
app = Flask(__name__)

connection = mysql.connector.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    database=os.getenv("DB_NAME")
)

cursor = connection.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS pets(id INT AUTO_INCREMENT PRIMARY KEY, name text, species text, age int, owner text)")

connection.commit()


cursor.execute("INSERT INTO pets(name, species, age, owner) VALUES ('mekus', 'cat', 4, 'renan');")

connection.commit()

cursor.execute("SELECT * FROM pets;")
pets = cursor.fetchall()
print(pets)

app.run(debug=False)