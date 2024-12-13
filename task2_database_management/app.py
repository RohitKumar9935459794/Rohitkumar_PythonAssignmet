# app.py
from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

# SQLite connection function
def get_db_connection():
    conn = sqlite3.connect('apps.db')
    conn.row_factory = sqlite3.Row
    return conn

# Fetch all apps
@app.route('/apps', methods=['GET'])
def get_apps():
    conn = get_db_connection()
    apps = conn.execute('SELECT * FROM apps').fetchall()
    conn.close()
    return jsonify([dict(app) for app in apps])

# Fetch a specific app by ID
@app.route('/apps/<int:id>', methods=['GET'])
def get_app(id):
    conn = get_db_connection()
    app = conn.execute('SELECT * FROM apps WHERE id = ?', (id,)).fetchone()
    conn.close()
    if app is None:
        return jsonify({"error": "App not found"}), 404
    return jsonify(dict(app))

if __name__ == '__main__':
    app.run(debug=True)
