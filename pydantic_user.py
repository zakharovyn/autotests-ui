from pydantic import BaseModel


class User(BaseModel):
    id: int
    username: str
    email: str
    is_active: bool = True


user_date = {
    "id": 1,
    "username": "zara",
    "email": "zara.bond@gmail.com"
}

user = User(**user_date)
print(user)
print(user.is_active)


invalid_user_data = {
    "id": "one",
    "username": "zara",
    "email": "zara.bond@gmail.com"
}

invalid_user = User(**invalid_user_data)

try:
    invalid_user = User(**invalid_user_data)
except Exception as e:
    print("Ошибка валидации:", e)
