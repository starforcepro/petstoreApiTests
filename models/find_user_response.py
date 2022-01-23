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

    def __init__(self, id=None, username=None, firstName=None, lastName=None, email=None, password=None, phone=None,
                 userStatus=None, code=None, type=None, message=None, status_code=None):
        super(FindUserResponse, self).__init__(code, type, message, status_code)
        self.id = id
        self.username = username
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        self.phone = phone
        self.userStatus = userStatus
