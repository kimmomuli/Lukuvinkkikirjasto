import unittest
from repositories.user_repository import user_repository


class TestUserRepository(unittest.TestCase):
    def setUp(self):
        user_repository.delete_all()
        user_repository.add_user("username", "password")

    def test_logging_in_with_correct_username_and_password(self):
        result = user_repository.login("username", "password")
        self.assertTrue(result)

    def test_logging_in_with_wrong_username(self):
        result = user_repository.login("wrong_username", "password")
        self.assertFalse(result)

    def test_logging_in_with_wrong_password(self):
        result = user_repository.login("username", "wrong_password")
        self.assertFalse(result)

    def test_user_exists_method_when_user_exists(self):
        result = user_repository.user_exists("username")
        self.assertTrue(result)

    def test_user_exists_method_when_user_doesnt_exist(self):
        result = user_repository.user_exists("nonexistent_username")
        self.assertFalse(result)
