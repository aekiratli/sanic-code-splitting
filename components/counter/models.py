from tortoise import fields
from tortoise.models import Model
from components.user.models import User

class Counter(Model):
    id = fields.IntField(pk=True)
    how_many_logged_in = fields.IntField(default=0)
    user: fields.ForeignKeyRelation["User"] = fields.ForeignKeyField("models.User", related_name="user")
