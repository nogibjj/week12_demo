from fastapi import FastAPI

import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/multiply/{a]/{b}")
async def func(a: int, b: int):
    result = a * b
    return result


if __name__ == "__main__":
    uvicorn.run(app, port=8080, host="0.0.0.0")
