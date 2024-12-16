from fastapi import FastAPI
from fastapi.responses import FileResponse

from contextlib import asynccontextmanager
from sqlmodel import SQLModel
import uvicorn


from db import engine

import sys, os
sys.path.insert(0, os.path.dirname(__file__))

from routers import cars

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

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    """Serves the icon file"""
    path  = os.path.join(os.path.dirname(__file__), 'static', 'favicon.ico')
    print(path)
    return FileResponse(path)


if __name__ == "__main__":
    uvicorn.run("car_sharing:app", reload=True)
