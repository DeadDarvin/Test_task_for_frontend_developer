from fastapi.responses import JSONResponse
from fastapi.routing import APIRouter
from custom_logger import get_custom_loger
from pydantic import BaseModel
from pydantic import Field


test_router = APIRouter()
logger = get_custom_loger("test")


class GeoJsonRequest(BaseModel):
    lat: float = Field(examples=[52.121147])
    lon: float = Field(examples=[42.212354])


class CustomResponse(BaseModel):
    success: bool = Field(examples=[True])
    description: str = Field(examples=["To be or not to be?"])


@test_router.get("/")
def ping_handler():
    return JSONResponse(content={"success": True}, status_code=200)


@test_router.post("/", response_model=CustomResponse)
def print_cords_in_logs(body: GeoJsonRequest):
    logger.error(f"Широта: {body.lat} || Долгота: {body.lon}")
    return CustomResponse(success=True, description="Yeah man, you're so good developer!")
