from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router.product import routerProduct
from router.user import routerUser
from router.contact import routerContact
from router.health_check import routerHealthCheck
import uvicorn

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
)

app.include_router(
    routerUser,
    prefix="/users",
    tags=["User Docs"],
)
app.include_router(
    routerProduct,
    prefix="/products",
    tags=["Product Docs!"],
)
app.include_router(
    routerContact,
    prefix="/contacts",
    tags=["Contact Docs!"],
)
app.include_router(
    routerHealthCheck,
    prefix="",
    tags=["Health Check Docs!"],
)

if __name__ == "__main__":
    uvicorn.run(app)
    app.run(debug=True)
