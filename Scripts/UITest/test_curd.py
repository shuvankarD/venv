import pytest
from typing import Generator

from playwright.sync_api import *


@pytest.fixture
def api_context(playwright: Playwright) -> Generator[APIRequestContext, None, None]:
    api_context = playwright.request.new_context(
        base_url="https://dummyjson.com"
        
    )
    yield api_context
    api_context.dispose()

def test_create_user(api_context: APIRequestContext):
    
    response = api_context.post(
     "users/add",
     headers = {'Content-Type':'application/json'},
    
     data = {
         "firstName": "Damien",
         "lastName": "Smith",
         "age":27
     }

    )
    user_data = response.json()
    print(f"{user_data}")
    assert user_data["firstName"]== "Damien"
    

def test_update_user(api_context: APIRequestContext):
    print(api_context.get("users/1").json()["lastName"])

    response= api_context.put(

        "users/1",
        headers = {'Content-Type':'application/json'},
        data={
            "lastName":"Dash",
            "age":29
        }
    )

    user_data = response.json()
    print(f"{user_data}")
    assert user_data["lastName"]== "Dash"

def test_delete_user(api_context: APIRequestContext):

    response = api_context.delete("users/1")

    user_data = response.json()

    print(f"{user_data}")

    