import pytest
from utils.api import APIS
import uuid

@pytest.fixture(scope='module')
def apis():
    return APIS()


def test_get_users(apis):
    response=apis.get('users')
    print(response.json())
    assert response.status_code == 200
    assert len(response.json()) > 0

def test_create_users(apis,load_user_data):
        # user_data={
        #     "name":"gio",
        #     "username":"scheo",
        #     "email": "gio@hotmail.com"
        # }
    user_data = load_user_data["new_user"]
    unique_email=f"{uuid.uuid4().hex[:8]}@hotmail.com"
    print(unique_email)
    user_data["email"]=unique_email

    response=apis.post('users',user_data)
    print(response.json())
    assert response.status_code == 201
    assert response.json()['name'] == 'gio'
    id=response.json()['id']
    responseget=apis.get('users/10')
    print(responseget.json())
    assert responseget.status_code == 200


def test_update_users(apis):
    user_data={
        "name":"mak",
        "username":"scheo",
        "email": "gio@hotmail.com"
    }
    response=apis.put('users/1',user_data)
    print(response.json())
    assert response.status_code == 200
    assert response.json()['name'] == 'mak'
 
def test_delete_users(apis):
    response=apis.delete('users/1')
    print(response.json())
    assert response.status_code == 200
 
