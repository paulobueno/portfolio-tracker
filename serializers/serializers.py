from sqlmodel import SQLModel
from datetime import date
from models.models import AssetCategory, TransactionType


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
    category_id: int | None


class AssetOut(SQLModel):
    id: int
    name: str
    ticker: str
    description: str | None
    detail: str | None
    category: AssetCategory | None


class TransactionCreate(SQLModel):
    asset_id: int
    quantity: float
    price: float
    date: date
    transaction_type: TransactionType


class TransactionOut(SQLModel):
    id: int
    asset: AssetOut
    quantity: float
    price: float
    date: date
    transaction_type: TransactionType
