import unittest
from services.user_service import UserService


class StubUserRepository:
    def __init__(self) -> None:
        self.users = []

    def user_exists(self, username: str) -> bool:
        for user in self.users:
            if user[0] == username:
                return True
        return False

    def add_user(self, username: str, password: str) -> None:
        self.users.append((username, password))

    def login(self, username: str, password: str) -> bool:
        for user in self.users:
            if user[0] == username and user[1] == password:
                return True
        return False


class TestUserService(unittest.TestCase):
    def setUp(self):
        self.user_service = UserService(StubUserRepository())

    def test_registering_with_valid_inputs_succeeds(self):
        error = self.user_service.register("username", "password")
        self.assertEqual(error, "")

    def test_registering_with_too_short_username_fails(self):
        error = self.user_service.register("us", "password")
        self.assertEqual(
            error, "Kayttäjätunnuksen on oltava vähintään 4 merkkiä pitkä"
        )

    def test_registering_with_too_short_password_fails(self):
        error = self.user_service.register("username", "passw")
        self.assertEqual(
            error, "Salasanan on oltava vähintään 6 merkkiä pitkä"
        )

    def test_register_and_login(self):
        self.user_service.register("username", "password")
        error = self.user_service.login("username", "password")
        self.assertEqual(error, "")

    def test_logging_in_with_wrong_username_fails(self):
        self.user_service.register("username", "password")
        error = self.user_service.login("wrong", "password")
        self.assertEqual(error, "Väärä käyttäjätunnus tai salasana")

    def test_logging_in_with_wrong_password_fails(self):
        self.user_service.register("username", "password")
        virheviesti = self.user_service.login("username", "wrong")
        self.assertEqual(virheviesti, "Väärä käyttäjätunnus tai salasana")

    def test_registering_with_existing_username_fails(self):
        self.user_service.register("username", "password")
        error = self.user_service.register("username", "password")
        self.assertEqual(error, "Käyttäjätunnus on jo olemassa")
