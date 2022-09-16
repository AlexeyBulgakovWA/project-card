from fastapi import FastAPI

app = FastAPI()


@app.get("/name")
async def root():
    return {"message": "Hello World" + "gfdkmokoefgsd"}
