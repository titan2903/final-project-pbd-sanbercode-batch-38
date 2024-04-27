from fastapi import APIRouter
from starlette.requests import Request
from controllers.user import UserController as controller
from fastapi import Depends
from middleware.auth_bearer import JWTBearer 

routerUser = APIRouter()

@routerUser.post("/", tags=["users"])
async def action(request: Request):
    return await controller.store(request)

@routerUser.put("/{id}", dependencies=[Depends(JWTBearer())], tags=["users"])
async def action(id: int, request: Request):
    return await controller.update(id, request)

@routerUser.post("/login", tags=["users"])
async def action(request: Request):
    return await controller.login(request)

@routerUser.get("/{id}", dependencies=[Depends(JWTBearer())], tags=["users"])
async def action(id: int, request: Request):
    return await controller.profile(id, request)
