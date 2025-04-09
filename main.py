from fastapi import FastAPI
from api.endpoints import router
from db.session import create_db_and_tables

app = FastAPI()
app.include_router(router)

@app.on_event("startup")
def on_startup():
    create_db_and_tables()


