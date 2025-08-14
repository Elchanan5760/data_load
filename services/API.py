from fastapi import FastAPI
from services.Dal import Dal
app = FastAPI()


my_dal = Dal(host,data_base,user,password,port)
@app.get("/")
def get_root():
    return {"Hello": "World"}

@app.get("/data")
def get_data():
    try:
        data = my_dal.select_all()
        return data
    except Exception as ex:
        print(f'Error {ex}')