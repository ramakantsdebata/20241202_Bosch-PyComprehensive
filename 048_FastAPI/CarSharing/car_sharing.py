from fastapi import FastAPI
from fastapi.responses import FileResponse
from datetime import datetime
import os

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

@app.get("/")
def welcome():
    """Returns a warm welcome message"""
    return {"message": "Welcome to the Car sharing application"}

@app.get("/date")
def date():
    """returns the current datetime on the server"""
    return {"date": datetime.now()}


@app.get("/favicon.ico", include_in_schema=False)
def favicon():
    """Serves the icon file"""
    path  = os.path.join(os.path.dirname(__file__), 'static', 'favicon.ico')
    print(path)
    return FileResponse(path)
