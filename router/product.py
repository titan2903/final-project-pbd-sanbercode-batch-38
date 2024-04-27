from fastapi import APIRouter
from controllers.product import ProductController as controller
from typing import Optional

routerProduct = APIRouter()

@routerProduct.get("/", tags=["products"])
async def action():
  return await controller.show()

@routerProduct.get("/search", tags=["products"])
async def action(keyword: Optional[str] = None):
  return await controller.search(keyword)