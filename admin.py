import os

from gino_admin import create_admin_app

os.environ["GINO_ADMIN"] = "1"


os.environ["SANIC_DB_HOST"] = os.getenv("DB_HOST", "localhost")
os.environ["SANIC_DB_DATABASE"] = "test_db"
os.environ["SANIC_DB_USER"] = "user"
os.environ["SANIC_DB_PASSWORD"] = "pass"


os.environ["SANIC_ADMIN_USER"] = "admin"
os.environ["SANIC_ADMIN_PASSWORD"] = "1234"


current_path = os.path.dirname(os.path.abspath(__file__))


if __name__ == "__main__":

    from app.factory.db_setup import  db
    from app.core.model.models import Test
  
    create_admin_app(
        host="127.0.0.1",
        port= 5000,
        db=db,
        db_models=[Test],
          config={"presets_folder": os.path.join(current_path, "csv_to_upload")},
  )