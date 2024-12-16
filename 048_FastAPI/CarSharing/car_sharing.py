from fastapi import FastAPI
from fastapi.responses import FileResponse

from contextlib import asynccontextmanager
from sqlmodel import SQLModel
import uvicorn


from db import engine

import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from routers import cars
from routers import web

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



if __name__ == "__main__":
    uvicorn.run("car_sharing:app", reload=True)
