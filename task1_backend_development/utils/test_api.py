import requests

BASE_URL = "http://127.0.0.1:5000"

def test_add_app():
    payload = {
        "app_name": "Test App",
        "version": "1.0",
        "description": "This is a test app."
    }
    response = requests.post(f"{BASE_URL}/add-app", json=payload)
    print("Add App Response:", response.json())

def test_get_app(app_id):
    response = requests.get(f"{BASE_URL}/get-app/{app_id}")
    print("Get App Response:", response.json())

def test_delete_app(app_id):
    response = requests.delete(f"{BASE_URL}/delete-app/{app_id}")
    print("Delete App Response:", response.json())

if __name__ == "__main__":
    print("Testing Add App...")
    test_add_app()

    print("\nTesting Get App with ID 1...")
    test_get_app(1)

    print("\nTesting Delete App with ID 1...")
    test_delete_app(1)
