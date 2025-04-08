from sqlmodel import SQLModel
from models.models import AssetCategory


class AssetCategoryCreate(SQLModel):
    name: str


class AssetCategoryOut(SQLModel):
    id: int
    name: str


class AssetCreate(SQLModel):
    name: str
    ticker: str
    description: str | None
    detail: str | None
    category_id: int | None = None


class AssetOut(SQLModel):
    id: int
    name: str
    ticker: str
    description: str | None
    detail: str | None
    category: AssetCategory | None
