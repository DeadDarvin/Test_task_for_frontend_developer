import uvicorn
from fastapi import FastAPI
from fastapi.routing import APIRouter
from api import test_router

# create instance of the app
app = FastAPI(title="Test Task For Frontend Developer")

# create the instance for the routes
main_api_router = APIRouter()

# set routes to the app instance
main_api_router.include_router(test_router, prefix="/test", tags=["test-server"])

app.include_router(main_api_router)

if __name__ == "__main__":
    # run app on the host and port
    uvicorn.run(app, host="0.0.0.0", port=8887)
