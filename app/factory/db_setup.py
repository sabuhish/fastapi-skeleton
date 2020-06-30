from gino.ext.starlette import Gino
from app.utils.options import  settings
from datetime import datetime
from sqlalchemy_utils import UUIDType
import uuid
import  os

if os.environ.get("GINO_ADMIN"):
    from gino.ext.sanic import Gino

    db = Gino()
    
else:
    db = Gino(
        dsn=settings.DB_DSN)

#  pool_min_size=settings.DB_POOL_MIN_SIZE,
#     pool_max_size=settings.DB_POOL_MAX_SIZE,
#     echo=settings.DB_ECHO,
#     ssl=settings.DB_SSL,
#     use_connection_for_request=settings.DB_USE_CONNECTION_FOR_REQUEST,

Integer, String,BOOLEAN, DateTime, Column,ForeignKey =  db.Integer, db.String,db.BOOLEAN, db.DateTime, db.Column,db.ForeignKey



class Model(db.Model):
    __abstract__ = True

    __table_args__ = {"extend_existing": True}


    id = Column(UUIDType(binary=False), primary_key=True,unique=True, default=uuid.uuid4)

    created_at = Column(DateTime, default=datetime.utcnow, server_default=db.func.now())

    updated_at = Column(DateTime,default=datetime.utcnow,onupdate=datetime.utcnow,server_default=db.func.now())

