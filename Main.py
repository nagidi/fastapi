from fastapi import FastAPI

app = FastAPI()
<<<<<<< Updated upstream
//
// fast api cooking
=======

#fast api cooking
#edit
>>>>>>> Stashed changes
@app.get("/")
async def root():
    return {"message": "Hello World"}