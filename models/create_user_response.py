from requests import Response

from models.api_response import ApiResponse


class CreateUserResponse(ApiResponse):
    @classmethod
    def build_from(cls, raw_api_response: Response):
        super().build_from(raw_api_response)

        return cls
