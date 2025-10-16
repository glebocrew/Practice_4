from datetime import datetime
from hashlib import sha512
from uuid import uuid4

from db.models.user_model import UserModelSQL as User
from db.orm.connect import Session, engine
from logger import Logger

db_logger = Logger(filepath="logs/db_log.txt")


class Database:
    def __hash_password(self, string: str) -> str:
        """
        Hashes any string
        """
        hash_object = sha512()
        hash_object.update(string.encode("utf-8"))

        return hash_object.hexdigest()

    def create_user(self, username: str, email: str, password: str) -> int:
        """
        Creates new user.
        Required: username, email, password
        Returned: 0/-1 code whether OK or failed
        """
        new_user = User(
            id=str(uuid4()),
            username=username,
            email=email,
            pwd=self.__hash_password(password),
            createdAt=str(datetime.now()),
            editedAt=str(datetime.now()),
        )

        db_logger.log("l", "Creating new user")
        try:
            with Session(engine) as session:
                session.add(new_user)
                session.commit()
        except Exception as exception:
            db_logger.log("e", f"Failed! Full exception -> {exception}")
            return -1

        db_logger.log("l", "User was created successfully")

        return 0
