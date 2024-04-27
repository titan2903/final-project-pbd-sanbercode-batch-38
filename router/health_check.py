from fastapi import APIRouter
from controllers.health_check import HealthController as controller

routerHealthCheck = APIRouter()

@routerHealthCheck.get("/", tags=["health_check"])
async def action():
  return await controller.health()