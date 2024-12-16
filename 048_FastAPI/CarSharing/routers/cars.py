from fastapi import HTTPException
from fastapi import Depends
from fastapi import APIRouter
from sqlmodel import Session, select

from schemas import CarDbModel, CarInput
from schemas import CarOutput
from schemas import TripInput, TripOutput
from schemas import TripDbModel
from schemas import User_DBModel
from schemas import load_lib

from db import get_session

from routers.auth import get_current_user


db = load_lib()

router = APIRouter(prefix="/api/cars")


@router.get("/")
def get_cars(size: str|None = None, doors: int|None = None, session: Session = Depends(get_session))->list[CarOutput]:  #->list[CarDbModel]:   #
    """Returns a list of cars from the server records"""
    query = select(CarDbModel)
    if size:
        query = query.where(CarDbModel.size == size)
    if doors:
        query = query.where(CarDbModel.doors == doors)

    result = session.exec(query).all()

    if result:
        return result
    else:
        raise HTTPException(status_code=404, detail=f"No car with size={size} and doors={doors}.")


@router.get("/{id}")
def get_car_by_id(id: int, session: Session = Depends(get_session))->CarOutput:         # ->list[CarDbModel]:   #
    """Returns a car matching the provided 'id' from the server records"""
    car = session.get(CarDbModel, id)
    if car:
        return car
    else:
        raise HTTPException(status_code=404, detail=f"No car with id {id} found on the server.")


@router.post("/", response_model=CarOutput)
def add_car(car: CarInput, session: Session = Depends(get_session),
            user: User_DBModel = Depends(get_current_user)) -> CarOutput:
    new_car = CarDbModel.model_validate(car)
    session.add(new_car)
    session.commit()
    session.refresh(new_car)
    return new_car


@router.delete("/{id}", status_code=204)
def remove_car(id: int, session: Session = Depends(get_session)) -> None:
    car = session.get(CarDbModel, id)
    if car:
        session.delete(car)
        session.commit()
    else:
        raise HTTPException(status_code=404, detail=f"No car with id {id} found.")

## Modify the preexisting object of a Car, by id
@router.put("/{id}", response_model=CarOutput)
def change_car(id: int, new_data: CarInput, session: Session = Depends(get_session)) -> CarOutput:
    car = session.get(CarDbModel, id)
    if car:
        car.fuel = new_data.fuel
        car.size = new_data.size
        car.doors = new_data.doors
        car.transmission = new_data.transmission

        session.commit()
        return car
    else:
        raise HTTPException(status_code=404, detail=f"No car with id={id}.")


class BadTripException(Exception):  # Custom Exception Class
    pass


# Add trip to an existing Car object
@router.post("/{car_id}/trips", response_model=TripOutput)
def add_trip(car_id: int, trip: TripInput, session: Session = Depends(get_session)) -> TripOutput:
    car = session.get(CarDbModel, car_id)
    if car:
        new_trip = TripDbModel.model_validate(trip, update={'car_id': car.id, 'id': None})
        if new_trip.start > new_trip.end:
            raise BadTripException("Trip end is before the start")
        car.trips.append(new_trip)
        session.commit()
        session.refresh(new_trip)
        return new_trip
    else:
        raise HTTPException(status_code=404, detail=f"No car with id {car_id} found.")

@router.delete("/{car_id}/trips/{trip_id}", status_code=204)
def remove_trip(car_id: int, trip_id:int, session: Session = Depends(get_session)) -> None:
    car = session.get(CarDbModel, car_id)
    if car:
        for trip in car.trips:
            if trip.id == trip_id:
                session.delete(trip)
                session.commit()
                return 
        else:
            raise HTTPException(status_code=404, detail=f"No trip with id {trip_id} found.")
    else:
        raise HTTPException(status_code=404, detail=f"No car with id {car_id} found.")

## Migrate the data from the json file to the Database ########################

@router.post("/migrate")
def migrate_data_to_db(session: Session = Depends(get_session)) -> list[CarOutput]:
    lstCars = []
    for car in db:
        new_car = CarDbModel.model_validate(car, update={'trips': []})
        session.add(new_car)

        session.commit()

        session.refresh(new_car)
        for trip in car.trips:
            new_trip = TripDbModel.model_validate(trip, update={'car_id': new_car.id, 'id': None})
            session.add(new_trip)
            session.commit()
            session.refresh(new_car)
        lstCars.append(new_car)
    return lstCars
