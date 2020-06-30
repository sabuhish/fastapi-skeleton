from pydantic import BaseSettings as Settings
from pydantic import  SecretStr, DirectoryPath
from pathlib import Path

current_file = Path(__file__)

current_file_dir = current_file.parent

project_root = current_file_dir.parent

project_root_absolute = project_root.resolve()

BASE_DIR = project_root_absolute.parent


class BaseSettings(Settings):
    title: str = "FastApi project sketelon"
    version: str = "0.0.1"
    description: str = "FastApi sketelon"
    docs_url: str = "/swagger"
    INCLUDE_SCHEMA: bool =False

    TEMPLATES_DIR: DirectoryPath = BASE_DIR / "templates"
    MEDIA_PATH: DirectoryPath = BASE_DIR / "media"
    STATIC_PATH: DirectoryPath = BASE_DIR / "static"    


# ["add_api_route', 'add_api_websocket_route', 'add_event_handler', 'add_exception_handler', 'add_middleware', 'add_route', 'add_websocket_route', 'api_route', 'build_middleware_stack', , 'default_response_class', , 'dependency_overrides', 'description', , 'exception_handler', 'exception_handlers', 'extra', '', , , 'include_router', 'middleware', 'middleware_stack', '', '', 'openapi', 'openapi_schema', 'openapi_tags', 'openapi_url', 'openapi_version','redoc_url', 'root_path', 'route', 'router', 'routes', 'servers', 'setup', 'state', 'swagger_ui_init_oauth', 'swagger_ui_oauth2_redirect_url', 'trace', 'url_path_for', 'user_middleware', ]




