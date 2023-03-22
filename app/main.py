from fastapi import FastAPI
from mangum import Mangum

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World_test"}

@app.get("/callname/{name}")
def read_name(name: str = None):
    return {"hello": name}

@app.post("/callname/{name}")
def post_name(name: str = None):
    return {"hello": name}

handler = Mangum(app)