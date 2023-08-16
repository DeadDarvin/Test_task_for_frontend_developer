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


class LogsResponse(BaseModel):
    logs: list[str]


@test_router.get("/")
def ping_handler():
    return JSONResponse(content={"success": True}, status_code=200)


@test_router.post("/", response_model=CustomResponse)
def print_cords_in_logs(body: GeoJsonRequest):
    logger.info(f"Широта: {body.lat} || Долгота: {body.lon}")
    return CustomResponse(success=True, description="Yeah man, you're so good developer!")


@test_router.get("/logs", response_model=LogsResponse)
def get_logs():
    logs_list = []
    with open("test.log", "r") as f_o:
        for line in f_o:
            logs_list.append(line)

    return LogsResponse(logs=logs_list)
