import os
import socket
from flask import Flask, jsonify
import mysql.connector
from mysql.connector import Error

app = Flask(__name__)

def db_connection():
    return mysql.connector.connect(
        host=os.getenv("DB_HOST", "db"),
        port=int(os.getenv("DB_PORT", "3306")),
        user=os.getenv("DB_USER", "labuser"),
        password=os.getenv("DB_PASSWORD", "lab-password-change-me"),
        database=os.getenv("DB_NAME", "workload_lab"),
        connection_timeout=3,
    )

@app.get("/")
def index():
    return jsonify(
        service="container-security-lab-api",
        message="Hello from the Flask API",
        hostname=socket.gethostname(),
        endpoints=["/api/", "/api/health", "/api/db"]
    )

@app.get("/api/")
def api_index():
    return jsonify(message="API is responding", service="flask-api")

@app.get("/api/health")
def health():
    return jsonify(status="ok"), 200

@app.get("/api/db")
def db_check():
    try:
        connection = db_connection()
        cursor = connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM lab_messages")
        count = cursor.fetchone()[0]
        cursor.close()
        connection.close()
        return jsonify(database="connected", message_count=count), 200
    except Error as exc:
        # Demo endpoint: do not expose raw database errors in a real application.
        return jsonify(database="unavailable", detail=str(exc)), 503

@app.post("/api/message")
def create_message():
    try:
        connection = db_connection()
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO lab_messages (message) VALUES (%s)",
            ("Hello from the container security lab",)
        )
        connection.commit()
        cursor.close()
        connection.close()
        return jsonify(created=True), 201
    except Error:
        return jsonify(created=False, error="Database operation failed"), 503

if __name__ == "__main__":
    # Flask's built-in server is acceptable for this isolated training lab only.
    app.run(host="0.0.0.0", port=5000)
