# Requirements
## Prerequisites
Python 3.8 or higher
pip (Python package manager)
Python Libraries

## Install the following Python libraries:

Flask
Flask-SQLAlchemy
requests (for testing via Python)
Setup
Clone or Download the Repository
Clone or download this project to your local machine:


## Install Dependencies
Install the required Python libraries using:

## pip install -r requirements.txt
If no requirements.txt is provided, install manually:


## pip install flask flask-sqlalchemy requests
Run the Application
## Start the Flask server:

python app.py
You should see output like:
* Running on http://127.0.0.1:5000 (Press CTRL+C to quit)
API Endpoints
1. Add App
URL: POST /add-app
Description: Add app details to the database.
Request Body (JSON):
json
Copy code
{
    "app_name": "Test App",
    "version": "1.0",
    "description": "This is a test app."
}
Response:
json
Copy code
{
    "app_id": 1,
    "message": "App added successfully"
}
2. Get App
URL: GET /get-app/<id>
Description: Retrieve app details by ID.
Response (Success):
json
Copy code
{
    "id": 1,
    "app_name": "Test App",
    "version": "1.0",
    "description": "This is a test app."
}
Response (Failure):
json
Copy code
{
    "error": "App not found"
}
3. Delete App
URL: DELETE /delete-app/<id>
Description: Remove an app by ID.
Response:
json
Copy code
{
    "message": "App deleted successfully"
}
Testing the API
Using Python Script
Run the utils/test_api.py script:

python utils/test_api.py
Expected Output:

## Add App:
json

{"app_id": 1, "message": "App added successfully"}

## Get App:
json

{"id": 1, "app_name": "Test App", "version": "1.0", "description": "This is a test app."}

## Delete App:
json


{"message": "App deleted successfully"}
Using Curl Commands
Alternatively, you can test using curl:

## Add App:

curl -X POST http://127.0.0.1:5000/add-app -H "Content-Type: application/json" -d '{"app_name": "Test App", "version": "1.0", "description": "This is a test app."}'
## Get App:
curl -X GET http://127.0.0.1:5000/get-app/1
## Delete App:
curl -X DELETE http://127.0.0.1:5000/delete-app/1
Troubleshooting
Module Not Found: Install missing libraries using pip install <module_name>.
404 Error: Ensure you are accessing valid endpoints.
Database Issues: Ensure db.create_all() is executed at least once before making API requests.