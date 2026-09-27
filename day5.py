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


app.run(debug=True)