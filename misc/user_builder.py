import threading
import uuid

from models.user import User


class UserBuilder:
    user: User

    def fill_fields_with_random_values(self):
        self.user = User(
            id=uuid.uuid4().node,
            username=uuid.uuid4().hex,
            firstName=uuid.uuid4().hex,
            lastName=uuid.uuid4().hex,
            email=uuid.uuid4().hex,
            password=uuid.uuid4().hex,
            phone=uuid.uuid4().hex,
            userStatus=uuid.uuid4().time_mid)

        return self

    def build(self):
        return self.user
