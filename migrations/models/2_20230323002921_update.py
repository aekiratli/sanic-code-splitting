from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS "counter" (
    "id" SERIAL NOT NULL PRIMARY KEY,
    "how_many_logged_in" INT NOT NULL  DEFAULT 0,
    "user_id" INT NOT NULL REFERENCES "user" ("id") ON DELETE CASCADE
);;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        DROP TABLE IF EXISTS "counter";"""
