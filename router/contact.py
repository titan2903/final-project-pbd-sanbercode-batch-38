from fastapi import APIRouter
from controllers.contact import ContactController as controller
from starlette.requests import Request
from fastapi import Depends
from middleware.auth_bearer import JWTBearer 

routerContact = APIRouter()

@routerContact.post("/", dependencies=[Depends(JWTBearer())], tags=["contacts"])
async def action(request: Request):
    return await controller.store(request)

@routerContact.put("/{id}", dependencies=[Depends(JWTBearer())], tags=["users"])
async def action(id: int, request: Request):
    return await controller.update(id, request)

@routerContact.get("/{id}", dependencies=[Depends(JWTBearer())], tags=["users"])
async def action(id: int, request: Request):
    return await controller.getById(id, request)