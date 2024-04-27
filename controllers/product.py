from starlette.responses import JSONResponse
from dto.dto import ok
from dto.dto import badRequest
from transformers.ProductTransformer import transform
from models.product import Products
from database.config import SessionLocal

db=SessionLocal()

class ProductController:
    @staticmethod
    async def show() -> JSONResponse:
        try:
            products = db.query(Products).all()
            products = transform(products)
            return ok(products, 'Success Get Products!')
        except Exception as e:
            return badRequest('', f'{e}')
    
    @staticmethod
    async def search(keyword: str) -> JSONResponse:
        try:
            products = db.query(Products)
            
            if keyword:
                products = products.filter(Products.product_name.like("%" +keyword + "%"))
            
            products = products.all()
            
            products = transform(products)
            return ok(products, 'Success search Products!')
        except Exception as e:
            return badRequest('', f'{e}')