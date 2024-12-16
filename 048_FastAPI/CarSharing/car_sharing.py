from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi import HTTPException
from datetime import datetime
import os

import uvicorn

import sys
# sys.path.insert(0, os.path.dirname(__file__))
# print(sys.path)

from schemas import CarInput
from schemas import CarOutput
from schemas import load_lib
from schemas import save_lib


db = load_lib()


app = FastAPI()

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

if __name__ == "__main__":
    uvicorn.run("car_sharing:app", reload=True)
