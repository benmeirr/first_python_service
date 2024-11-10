from typing import Optional, List

from model.user import User
from model.user_request import UserRequest
from repository.database import database

TABLE_NAME = "users"


async def get_by_username(username: str) -> Optional[User]:
    query = f"SELECT * FROM {TABLE_NAME} WHERE username=:username AND is_active=:is_active"
    result = await database.fetch_one(query, values={"username": username, "is_active": True})
    if result:
        return User(**result)
    else:
        return None


async def get_by_id(user_id: int) -> Optional[User]:
    query = f"SELECT * FROM {TABLE_NAME} WHERE id=:user_id AND is_active=:is_active"
    result = await database.fetch_one(query, values={"user_id": user_id, "is_active": True})
    if result:
        return User(**result)
    else:
        return None


async def create_user(user: UserRequest, hashed_password: str):
    query = f"""
        INSERT INTO {TABLE_NAME} (username, first_name, last_name, hashed_password, is_active)
        VALUES (:username, :first_name, :last_name, :hashed_password, :is_active)
    """
    user_dict = user.dict()
    del user_dict["password"]
    values = {**user_dict, "hashed_password": hashed_password, "is_active": True}

    await database.execute(query, values)


async def get_users() -> List[User]:
    query = f"SELECT * FROM {TABLE_NAME} WHERE is_active=:is_active"
    results = await database.fetch_all(query, values={"is_active": True})
    return [User(**result) for result in results]
