from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.responses import FileResponse
from fastapi import HTTPException
from datetime import datetime
import os
from sqlmodel import SQLModel, create_engine

import uvicorn

import sys
# sys.path.insert(0, os.path.dirname(__file__))
# print(sys.path)

from schemas import CarInput
from schemas import CarOutput
from schemas import TripInput, TripOutput
from schemas import load_lib
from schemas import save_lib


# db = load_lib()


engine = create_engine(
    "sqllite:///carsharing.db",
    connect_args={"check_same_thread": False},
    echo=True
)


@asynccontextmanager
async def lifespan(app:FastAPI):
    # Create data table as per the specification in the schema
    SQLModel.metadata.create_all(engine)

    # Execute the app
    yield

    # Task to wind up
    print("That's all folks!")

app = FastAPI(title="Car Sharing App", description="An app to share cars.", lifespan=lifespan)




@app.get("/api/cars")
def get_cars(size: str|None = None, doors: int|None = None)->list[CarOutput]:
    """Returns a list of cars from the server records"""
    cars = db
    if size:
        cars = [car for car in cars if car.size == size]

    if doors:
        cars = [car for car in cars if car.doors == doors]

    return cars

@app.get("/api/cars/{id}")
def get_car_by_id(id: int)->CarInput:
    """Returns a car matching the provided 'id' from the server records"""
    result = [car for car in db if car.id == id]
    if result:
        return result[0]
    else:
        raise HTTPException(status_code=404, detail=f"No car with id {id} found on the server.")

@app.get("/favicon.ico", include_in_schema=False)
async def favicon():
    """Serves the icon file"""
    path  = os.path.join(os.path.dirname(__file__), 'static', 'favicon.ico')
    print(path)
    return FileResponse(path)

@app.post("/api/cars", response_model=CarOutput)
def add_car(car: CarInput) -> CarOutput:
    new_car = CarOutput(size=car.size, doors=car.doors,
                        fuel=car.fuel, transmission=car.transmission,
                        id=len(db)+1)
    db.append(new_car)
    save_lib(db)
    return new_car


@app.delete("/api/cars/{id}", status_code=204)
def remove_car(id: int) -> None:
    matches = [car for car in db if car.id == id]
    if matches:
        car = matches[0]
        db.remove(car)
        save_lib(db)
    else:
        raise HTTPException(status_code=404, detail=f"No car with id {id} found.")

## Modify the preexisting object of a Car, by id
@app.put("/api/cars/{id}", response_model=CarOutput)
def change_car(id: int, new_data: CarInput) -> CarOutput:
    matches = [car for car in db if car.id == id]
    if matches:
        car = matches[0]
        car.fuel = new_data.fuel
        car.size = new_data.size
        car.doors = new_data.doors
        car.transmission = new_data.transmission
        save_lib(db)
        return car
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id}.")


# Add trip to an existing Car object
@app.post("/api/cars/{id}/trips", response_model=TripOutput)
def add_trip(car_id: int, trip: TripInput) -> TripOutput:
    matches = [car for car in db if car.id == car_id]
    if matches:
        car = matches[0]
        new_trip = TripOutput(start=trip.start, end=trip.end,
                              description=trip.description, id=len(car.trips)+1)
        car.trips.append(new_trip)
        save_lib(db)
        return new_trip
    else:
        raise HTTPException(status_code=404, detail=f"No car with id {id} found.")

@app.delete("/api/cars/{car_id}/trips/{trip_id}", status_code=204)
def remove_car(car_id: int, trip_id:int) -> None:
    for car in db:
        if car.id == car_id:
            for trip in car.trips:
                if trip.id == trip_id:
                    car.trips.remove(trip)
                    save_lib(db)
                    return
    else:
        raise HTTPException(status_code=404, detail=f"No car with id {car_id} found.")


if __name__ == "__main__":
    uvicorn.run("car_sharing:app", reload=True)
