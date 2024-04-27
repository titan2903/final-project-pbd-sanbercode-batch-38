from starlette.responses import JSONResponse
from dto.dto import ok
from dto.dto import badRequest

class HealthController:
    @staticmethod
    async def health() -> JSONResponse:
        try:
            response = {
                "success": True,
            }
            return ok(response, "Server running successfully!")
        except Exception as e:
            return badRequest('', f'{e}')