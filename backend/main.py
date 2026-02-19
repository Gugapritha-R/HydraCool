from fastapi import FastAPI
from routes import predict


app=FastAPI()

'''
initial test
@app.get("/")
async def root():
    return{"message":"Hydracool backend is running"}

    '''



app.include_router(predict.router)