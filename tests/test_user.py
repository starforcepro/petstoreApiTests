import pytest
import pytest_check as c

from misc.pet_store_client import PetStoreClient
from misc.user_builder import UserBuilder
from models.user import User


class TestUser:

    @pytest.fixture
    def inserted_user(self):
        user = UserBuilder().fill_fields_with_random_values().build()
        PetStoreClient().user_actions().create(user)
        yield user
        PetStoreClient().user_actions().delete(user.username)

    @pytest.fixture
    def generated_user(self):
        user = UserBuilder().fill_fields_with_random_values().build()
        yield user
        PetStoreClient().user_actions().delete(user.username)

    def test_create_user(self, generated_user):
        create_user_response = PetStoreClient().user_actions().create(generated_user)

        c.equal(create_user_response.code, 200)
        c.equal(create_user_response.type, "unknown")
        c.equal(create_user_response.message, str(generated_user.id))

    # lets assume this endpoint has server side email validation just for example
    def test_create_user_when_email_is_incorrect(self, generated_user: User):
        generated_user.email = "incorrect_format_email"
        create_user_response = PetStoreClient().user_actions().create(generated_user)

        c.equal(create_user_response.code, 400)
        c.equal(create_user_response.type, "incorrect email")

    def test_find_user_by_username_when_user_exists(self, inserted_user):
        find_user_response = PetStoreClient().user_actions().find(inserted_user.username)

        c.equal(find_user_response.username, inserted_user.username)

    def test_find_user_by_username_when_user_does_not_exist(self):
        find_user_response = PetStoreClient().user_actions().find("nonexistent_username")

        c.equal(find_user_response.status_code, 404)
        c.equal(find_user_response.message, "User not found")
