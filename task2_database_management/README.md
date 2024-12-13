# Flask SQLite API

This is a simple API to demonstrate SQLite integration with Flask.

## Setup

1. Create a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate
Install dependencies:


pip install -r requirements.txt
Create the database:


sqlite3 apps.db < schema.sql
Run the application:


python app.py
## Endpoints
GET /apps: Fetch all apps.
GET /apps/<id>: Fetch a specific app by ID.
yaml


---

## Commands Summary

```bash
# 1. Create project folder and navigate into it
mkdir project && cd project

# 2. Create schema file
nano schema.sql

# 3. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 4. Install dependencies
nano requirements.txt
pip install -r requirements.txt

# 5. Create SQLite database
sqlite3 apps.db < schema.sql

# 6. Create Flask app
nano app.py

# 7. Run the Flask app
python app.py

# 8. Test the API
curl http://127.0.0.1:5000/apps
curl http://127.0.0.1:5000/apps/1
