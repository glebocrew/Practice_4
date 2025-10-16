from sys import exit

from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

from consts import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER
from logger import Logger

db_logger = Logger(filepath="logs/db_log.txt")

CONNECTION_STRING = (
    f"mariadb+mariadbconnector://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

db_logger.log("l", "Creating ORM Engine")
try:
    engine = create_engine(CONNECTION_STRING)
except Exception as exception:
    db_logger.log("f", f"Cannot create engine. Full exception --> {exception}")
    exit(-1)
db_logger.log("l", "Successfully created engine!")


if __name__ == "__main__":
    with Session(engine) as session:
        session.execute(statement=text("SELECT 1"))

        session.commit()
        session.close()
