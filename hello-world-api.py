from fastapi import FastAPI

app = FastAPI()

@app.get("/teste")
async def hello_world():
    return {'Hello fastapi world'}