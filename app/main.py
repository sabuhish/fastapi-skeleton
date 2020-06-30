from app.core.controller.routers.api.v1 import  api
from app.core.controller.routers.views.app import  router
from starlette.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.factory.app_factory import app_setting, Customexception
from starlette.applications import Starlette
from app.utils.options import  MOUNTS
from app.factory.db_setup import  db
from app.core.model.models import *
from app.utils.options import API_V1, TAGS, settings, media, static
from fastapi.staticfiles import StaticFiles


if app_setting() is None: raise Customexception("settings should be either dev or prod")

# print(app_setting().dict())

app = FastAPI(**app_setting().dict())


db.init_app(app)

app.include_router(router)


app.include_router(api, prefix=API_V1, tags=TAGS)


app.mount(static, StaticFiles(directory=settings.STATIC_PATH), name="static")

app.mount(media, StaticFiles(directory=settings.MEDIA_PATH), name="media")


@app.on_event("startup")
async def startup():
    print("app started")


@app.on_event("shutdown")
async def shutdown():
    """
    Pops the bind on the db object.
    """
    await db.pop_bind().close()
    print("SHUTDOWN")


app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_HOSTS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
