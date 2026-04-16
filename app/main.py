from fastapi import FastAPI
from app.core.exception_handler import global_exception_handler
from app.apis.indusemployee import router

app = FastAPI()

app.include_router(router, prefix="/indus", tags=["Employees"])

app.add_exception_handler(Exception, global_exception_handler)