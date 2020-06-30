from pydantic import BaseModel, Field



class TestSchema(BaseModel):
    status: bool
