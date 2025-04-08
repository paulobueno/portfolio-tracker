from typing import Annotated
from fastapi import FastAPI, Depends
from sqlmodel import SQLModel, Session, Relationship, Field, create_engine, text, select
from sqlalchemy.orm import selectinload
from models.models import AssetCategory, Asset
from serializers.serializers import AssetCategoryCreate, AssetCategoryOut, AssetCreate, AssetOut


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
    with engine.connect() as connection:
        connection.execute(text("PRAGMA foreign_keys=ON"))


def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.get("/asset/")
async def list_assets(session: SessionDep) -> list[AssetOut]:
    stmt = select(Asset)
    assets = session.exec(stmt).all()
    return assets

@app.post("/asset/")
async def create_asset(asset: AssetCreate, session: SessionDep) -> AssetOut:
    db_asset = Asset.model_validate(asset)
    session.add(db_asset)
    session.commit()
    session.refresh(db_asset)
    return db_asset

@app.get("/asset-category/")
async def list_asset_categories(session: SessionDep) -> list[AssetCategoryOut]:
    asset_cateogry = session.exec(select(AssetCategory)).all()
    return asset_cateogry

@app.post("/asset-category/")
async def create_asset_category(asset_category: AssetCategoryCreate, session: SessionDep) -> AssetCategoryOut:
    db_asset_category = AssetCategory.model_validate(asset_category)
    session.add(db_asset_category)
    session.commit()
    session.refresh(db_asset_category)
    return db_asset_category

