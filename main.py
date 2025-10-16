from db.orm import Database

db = Database()

create_status = db.create_user("glebocrew2", "glebocrew2@yandex.ru", "123")
print(create_status)
