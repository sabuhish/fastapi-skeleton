from fastapi import APIRouter

from fastapi import Request
from app.core.model.models import Test
from app.core.json.schemas import  TestSchema
from uuid import  UUID

api = APIRouter()

@api.post("/test")
async def test_api(test: TestSchema):
    print(test.dict())
    result = await  Test.create(**test.dict())
    return  result.to_dict()


@api.put("/test/update/{id}")
async def test_api(test: TestSchema, id:str=id):

    res = await  Test.query.where(Test.id==id).gino.first()

    await res.update(**test.dict()).apply()

    return res.to_dict()

@api.get("/test/get/{id}")
async def test_table(id: UUID):

    test = await Test.get_or_404(id)

    return test.to_dict()