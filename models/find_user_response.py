import json

from requests import Response

from models.api_response import ApiResponse


class FindUserResponse(ApiResponse):
    id: int
    username: str
    firstName: str
    lastName: str
    email: str
    password: str
    phone: str
    userStatus: int

    @classmethod
    def build_from(cls, raw_api_response: Response):
        user_dict = json.loads(raw_api_response.text)
        cls.id = user_dict.get('id')
        cls.username = user_dict.get('username')
        cls.firstName = user_dict.get('firstName')
        cls.lastName = user_dict.get('lastName')
        cls.email = user_dict.get('email')
        cls.password = user_dict.get('password')
        cls.phone = user_dict.get('phone')
        cls.userStatus = user_dict.get('userStatus')
        super().build_from(raw_api_response)

        return cls
