from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def hello():
    return {
        "message" : "Hello World"
        }

@app.get("/home/{name}")
def home(name : str):
    return{
        "message" : f"Hello, {name}!"
    }