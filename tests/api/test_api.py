import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"

class TestAPI:
    created_user_id = None

    def test_get_users(self):
        response = requests.get(f"{BASE_URL}/users")
        
        assert response.status_code == 200
        json_data = response.json()

        assert isinstance(json_data, list)
        assert len(json_data) > 0

    def test_create_user(self):
        payload = {
            "name": "Leanne Graham",
            "username": "Bret",
            "email": "Sincere@april.biz"
        }
        response = requests.post(f"{BASE_URL}/users", json=payload)
        
        assert response.status_code == 201
        json_data = response.json()

        assert "id" in json_data

        TestAPI.created_user_id = json_data["id"]

    def test_update_user(self):
        user_id_to_update = 1
        
        payload = {
            "name": "Usuario Actualizado",
            "username": "QA_Master"
        }
        
        response = requests.put(f"{BASE_URL}/users/{user_id_to_update}", json=payload)
        
        assert response.status_code == 200
        json_data = response.json()
        assert json_data["name"] == "Usuario Actualizado"

    def test_delete_user(self):
        response = requests.delete(f"{BASE_URL}/users/1")
        assert response.status_code == 200