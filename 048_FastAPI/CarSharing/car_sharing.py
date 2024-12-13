from fastapi import FastAPI
from fastapi.responses import FileResponse
from datetime import datetime
import os


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
