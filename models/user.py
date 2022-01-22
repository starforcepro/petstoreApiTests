import json


class User:
    id: int
    username: str
    firstName: str
    lastName: str
    email: str
    password: str
    phone: str
    userStatus: int

    def __init__(self, id: int, username: str, firstName: str, lastName: str, email: str, password: str, phone: str,
                 userStatus: int):
        self.id = id
        self.username = username
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        self.phone = phone
        self.userStatus = userStatus

    def to_json(self):
        return json.dumps(self.__dict__)
