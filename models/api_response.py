import json

from requests import Response


class ApiResponse:
    code: int
    type: str
    message: str
    status_code: int

    @classmethod
    def build_from(cls, raw_api_response: Response):
        create_user_response_dict = json.loads(raw_api_response.text)
        cls.code = create_user_response_dict.get('code')
        cls.type = create_user_response_dict.get('type')
        cls.message = create_user_response_dict.get('message')
        cls.status_code = raw_api_response.status_code

        return cls
