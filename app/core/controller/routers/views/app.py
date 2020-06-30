from fastapi import APIRouter
from app.utils.options import  templates

from fastapi import Request


router = APIRouter()

@router.get("/")
async def test(request: Request):
    world = "world"
    return templates.TemplateResponse("index.html", {"request": request ,"world": world}) 
    