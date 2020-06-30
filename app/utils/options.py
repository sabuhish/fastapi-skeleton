from fastapi.templating import Jinja2Templates
from app.factory.app_factory import  app_setting, Customexception
from fastapi.staticfiles import StaticFiles




settings = app_setting()

if settings is None: raise Customexception("settings should be dev or prod")

templates = Jinja2Templates(directory=settings.TEMPLATES_DIR)

MOUNTS = (
    ("/static", StaticFiles(directory=settings.STATIC_PATH), {"name":"static"}),
    ("/media", StaticFiles(directory=settings.MEDIA_PATH),{"name":"media"}),
)

static: str = "/static"

media: str = "/media"

API_V1: str = "/api/v1"

TAGS: list = ["api"]

