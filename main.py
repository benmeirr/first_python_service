from fastapi import FastAPI
from controller.user_controller import router as user_router
from controller.order_controller import router as order_router
from repository.database import database

app = FastAPI()


@app.on_event("startup")
def startup():
    database.connect()


@app.on_event("shutdown")
def shutdown():
    database.disconnect()


app.include_router(user_router)
app.include_router(order_router)
