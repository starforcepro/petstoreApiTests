import json

from requests import Response


class ApiResponse:
    code: int
    type: str
    message: str
    status_code: int

    def __init__(self, code=None, type=None, message=None, status_code=None):
        self.code = code
        self.type = type
        self.message = message
        self.status_code = status_code

    @classmethod
    def build_from(cls, raw_api_response: Response):
        if not raw_api_response.text:
            return cls(status_code=raw_api_response.status_code)

        instance = cls(**json.loads(raw_api_response.text))
        instance.status_code = raw_api_response.status_code

        return instance
