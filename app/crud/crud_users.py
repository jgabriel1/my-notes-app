from typing import Optional

from databases import Database

from ..database import users_table
from ..schemas import UserSchema
from ..security.hash import hash_password, verify_password


async def register_new(database: Database, user: UserSchema) -> None:
    query = users_table.insert().values(
        username=user.username,
        password=hash_password(user.password)
    )
    await database.execute(query)


async def get_info(database: Database, username: str) -> Optional[UserSchema]:
    query = users_table.select().where(
        users_table.c.username == username
    )
    user = await database.fetch_one(query)

    if user is not None:
        return UserSchema(**user)


async def authenticate(
        database: Database, username: str, password: str) -> Optional[UserSchema]:
    user = await get_info(database, username)
    if not user:
        return False
    if not verify_password(password, user.password):
        return False
    return user
