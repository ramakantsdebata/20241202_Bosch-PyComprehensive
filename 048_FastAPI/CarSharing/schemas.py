from sqlmodel import Field, SQLModel
from sqlmodel import Relationship
from pydantic import ConfigDict
import json
import os


class TripInput(SQLModel):
    start: int
    end:int
    description: str

class TripOutput(TripInput):
    id: int

class TripDbModel(TripInput, table=True):
    id: int|None = Field(default=None, primary_key=True)
    car_id: int = Field(foreign_key="cardbmodel.id")
    car: "CarDbModel" = Relationship(back_populates="trips")

class CarInput(SQLModel):
    size: str
    fuel: str = "electric"
    doors: int
    transmission: str = "auto"
    model_config = ConfigDict(
        json_schema_extra={
            "example": {
                "size": "Postman-size",
                "fuel": "tesla-battery",
                "doors": 5,
                "transmission":"automatic"
            }
        }
    )

class CarOutput(CarInput):
    id: int
    trips: list[TripOutput] = []

class CarDbModel(CarInput, table=True):
    id:int|None = Field(primary_key=True, default=None)
    trips: list[TripDbModel] = Relationship(back_populates="car")


json_file = "cars.json"
filePath = os.path.join(os.path.dirname(__file__), json_file)

def load_lib():
    """Loads the json data as objects into a collection"""
    with open(filePath, mode="r") as file:
        return [CarOutput.model_validate(obj)  for obj in json.load(file)]

def save_lib(cars):
    """Dumps the collection of objests into a json file"""
    with open(filePath, mode="w") as file:
        # json.dump(cars, file, indent=4)
        json.dump([car.model_dump() for car in cars], file, indent=4)


if __name__ == "__main__":
    c1 = CarInput(id=1, size="m", fuel="Petrol", doors=5, transmission="auto")
    c2 = CarInput(id=1, size="m", doors=5)

    print(c1.model_dump())              # print(c1.dict())
    print(c1.model_dump_json())         # print(c1.json())

