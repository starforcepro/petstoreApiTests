import requests

from models.create_user_response import CreateUserResponse
from models.find_user_response import FindUserResponse
from models.user import User


class PetStoreClient:
    base_url: str

    def __init__(self):
        self.base_url = "https://petstore.swagger.io/v2"

    def user_actions(self):
        return UserActions(self.base_url)


class UserActions:
    url: str

    def __init__(self, base_url):
        self.url = base_url + "/user"

    def create(self, user: User):
        headers = {'Content-type': 'application/json'}
        response = requests.post(self.url, data=user.to_json(), headers=headers)

        return CreateUserResponse.build_from(response)

    def find(self, username):
        response = requests.get(f"{self.url}/{username}")

        return FindUserResponse.build_from(response)

    def delete(self, username):
        headers = {'api_key': 'special_key'}
        requests.delete(f"{self.url}/{username}", headers=headers)
