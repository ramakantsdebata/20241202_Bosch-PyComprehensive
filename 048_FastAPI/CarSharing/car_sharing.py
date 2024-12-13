from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi import HTTPException
from datetime import datetime
import os

import uvicorn

db = [
    {"id": 1, "size": "s", "fuel": "petrol",    "doors": 3, "transmission": "auto"  },
    {"id": 2, "size": "s", "fuel": "electric",  "doors": 3, "transmission": "auto"  },
    {"id": 3, "size": "s", "fuel": "petrol",    "doors": 5, "transmission": "manual"},
    {"id": 4, "size": "m", "fuel": "electric",  "doors": 3, "transmission": "auto"  },
    {"id": 5, "size": "m", "fuel": "hybrid",    "doors": 5, "transmission": "auto"  },
    {"id": 6, "size": "m", "fuel": "petrol",    "doors": 5, "transmission": "manual"},
    {"id": 7, "size": "l", "fuel": "disel",     "doors": 5, "transmission": "manual"},
    {"id": 8, "size": "l", "fuel": "electric",  "doors": 5, "transmission": "auto"  },
    {"id": 9, "size": "l", "fuel": "hybrid",    "doors": 5, "transmission": "auto"  }
]

app = FastAPI()

# @app.get("/")
# def welcome(name):
#     """Returns a warm welcome message"""
#     return {"message": f"Hi {name}. Welcome to the Car sharing application"}

# @app.get("/date")
# def date():
#     """returns the current datetime on the server"""
#     return {"date": datetime.now()}

@app.get("/api/cars")
def get_cars(size: str|None = None, doors: int|None = None)->list:
    """Returns a list of cars from the server records"""
    cars = db
    if size:
        cars = [car for car in cars if car["size"] == size]

    if doors:
        cars = [car for car in cars if car["doors"] == doors]

    return cars

@app.get("/api/cars/{id}")
def get_cars(id: int) ->dict:
    """Returns a car matching the provided 'id' from the server records"""
    result = [car for car in db if car["id"] == id]
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

if __name__ == "__main__":
    uvicorn.run("car_sharing:app", reload=True)
