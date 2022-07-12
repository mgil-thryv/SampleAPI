from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.get("/")
def current_datetime():
    return {"datetime": datetime.now().strftime("%Y-%m-%d %H:%m:%s")}

@app.get("/time")
def time():
    return {"time": datetime.now().strftime("%H:%M:%s")}

@app.get("/date")
def date():
    return {"date": datetime.now().strftime("%Y-%m-%d")}