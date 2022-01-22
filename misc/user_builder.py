import threading
import uuid

from models.user import User


class UserBuilder:
    user: User

    def fill_fields_with_random_values(self):
        user_id = threading.current_thread().native_id
        self.user = User(
            id=user_id,
            username=uuid.uuid4().hex,
            firstName=uuid.uuid4().hex,
            lastName=uuid.uuid4().hex,
            email=uuid.uuid4().hex,
            password=uuid.uuid4().hex,
            phone=uuid.uuid4().hex,
            userStatus=uuid.uuid4().int % 10000)

        return self

    def set_email(self, email: str):
        self.user.email = email
        return self

    def build(self):
        return self.user
