from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)

# Get the absolute path to the current directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Updated SQLite database URI with an absolute path
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(BASE_DIR, "database", "apps.db")}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Ensure the database directory exists
os.makedirs(os.path.join(BASE_DIR, "database"), exist_ok=True)

db = SQLAlchemy(app)

# Define the App model
class App(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    app_name = db.Column(db.String(100), nullable=False)
    version = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(250), nullable=True)

# Initialize the database
with app.app_context():
    db.create_all()

# Endpoint: Add app details
@app.route('/add-app', methods=['POST'])
def add_app():
    data = request.json
    app_name = data.get('app_name')
    version = data.get('version')
    description = data.get('description')
    
    if not app_name or not version:
        return jsonify({'error': 'app_name and version are required'}), 400

    new_app = App(app_name=app_name, version=version, description=description)
    db.session.add(new_app)
    db.session.commit()

    return jsonify({'message': 'App added successfully', 'app_id': new_app.id}), 201

# Endpoint: Retrieve app details by ID
@app.route('/get-app/<int:id>', methods=['GET'])
def get_app(id):
    app_record = App.query.get(id)
    if not app_record:
        return jsonify({'error': 'App not found'}), 404

    return jsonify({
        'id': app_record.id,
        'app_name': app_record.app_name,
        'version': app_record.version,
        'description': app_record.description
    })

# Endpoint: Delete app by ID
@app.route('/delete-app/<int:id>', methods=['DELETE'])
def delete_app(id):
    app_record = App.query.get(id)
    if not app_record:
        return jsonify({'error': 'App not found'}), 404

    db.session.delete(app_record)
    db.session.commit()

    return jsonify({'message': 'App deleted successfully'})

if __name__ == '__main__':
    app.run(debug=True)
