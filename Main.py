from fastapi import FastAPI

app = FastAPI()
//
// fast api cooking
// nagid cooking
@app.get("/")
async def root():
    return {"message": "Hello World"}