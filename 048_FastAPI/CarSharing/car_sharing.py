from fastapi import FastAPI
from fastapi import Request
from fastapi.responses import FileResponse

from contextlib import asynccontextmanager
from sqlmodel import SQLModel
import uvicorn

from starlette.responses import JSONResponse
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY

from db import engine

import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from routers import cars
from routers import web
from routers import auth
from routers.cars import BadTripException

@asynccontextmanager
async def lifespan(app:FastAPI):
    # Create data table as per the specification in the schema
    SQLModel.metadata.create_all(engine)

    # Execute the app
    yield

    # Task to wind up
    print("That's all folks!")

app = FastAPI(title="Car Sharing App", description="An app to share cars.", lifespan=lifespan)
app.include_router(cars.router)
app.include_router(web.router)
app.include_router(auth.router)


@app.exception_handler(BadTripException)
async def uvicorn_exception_handler(request: Request, exc: BadTripException):
    return JSONResponse(
        status_code=HTTP_422_UNPROCESSABLE_ENTITY,
        content={"message": "Bad trip"}
    )


@app.middleware("http")
async def add_cars_cookie(request: Request, call_next):
    response = await call_next(request)
    response.set_cookie(key="cars_cookie", value="you_visited_the_carsharing_app")
    return response


if __name__ == "__main__":
    uvicorn.run("car_sharing:app", reload=True)
