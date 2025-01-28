from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)


# Connexion à la base de données PostgreSQL
def get_db_connection():
    conn = psycopg2.connect(
        host="db", database="mydb", user="user", password="password"
    )
    return conn


@app.route("/")
def hello_world():
    return "Hello, Docker Compose!"


@app.route("/users")
def get_users():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users;")
    users = cursor.fetchall()
    conn.close()
    return jsonify(users)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
