from sanic import Sanic
from backends.postgre import APPS_MODELS, connect_database
from tortoise import Tortoise
from components.user.views import users
from components.counter.views import counter
from sanic import Blueprint
from middleware.auth import authentication

def create_app() -> Sanic:
    Tortoise.init_models(APPS_MODELS, "models")
    app = Sanic("SplittingApp")
    group = Blueprint.group(
        users,
        counter,
        version_prefix="/api/v",
        version=1,
    )

    group.middleware(authentication, "request")
    app.blueprint(group)
    connect_database(app)
    return app
