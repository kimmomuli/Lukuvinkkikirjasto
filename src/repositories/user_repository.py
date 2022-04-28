from werkzeug.security import check_password_hash, generate_password_hash
from database import database


class UserRepository:
    def user_exists(self, username: str) -> bool:
        sql = """SELECT username
                 FROM users
                 where username = :username"""
        result = database.session.execute(sql, {"username": username})
        return bool(result.fetchone())

    def add_user(self, username: str, password: str) -> None:
        password_hash = generate_password_hash(password)
        sql2 = """INSERT into users (username, password)
                  VALUES (:username, :password)"""
        database.session.execute(
            sql2, {"username": username, "password": password_hash}
        )
        database.session.commit()

    def login(self, username: str, password: str) -> bool:
        sql = """SELECT password
                 FROM users
                 WHERE username = :username"""
        result = database.session.execute(
            sql, {"username": username}).fetchone()
        if result:
            return check_password_hash(result[0], password)

        return False

    def delete_all(self) -> None:
        sql = "DELETE FROM users"
        database.session.execute(sql)
        database.session.commit()


user_repository = UserRepository()
