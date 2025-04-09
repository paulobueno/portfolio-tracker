from enum import Enum

from sqlmodel import SQLModel, Relationship, Field
from datetime import date

class AssetCategory(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field()
    assets: list['Asset'] | None = Relationship(back_populates="category")


class Asset(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field()
    ticker: str = Field(index=True)
    description: str | None = Field(default=None)
    detail: str | None = Field(default=None)
    category_id: int | None = Field(default=None, foreign_key="assetcategory.id")
    category: AssetCategory | None = Relationship(back_populates="assets")
    transactions: list['Transaction'] | None = Relationship(back_populates="asset")


class AssetEndpoint(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    description: str | None = Field(default=None)
    status: str | None = Field(default='active')
    url: str | None = Field(default=None)
    asset_id: int = Field(foreign_key="asset.id")


class TransactionType(str, Enum):
    BUY = "buy"
    SELL = "sell"


class Transaction(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    asset_id: int = Field(foreign_key="asset.id")
    asset: Asset = Relationship(back_populates="transactions")
    quantity: float
    price: float
    date: date
    transaction_type: TransactionType


class PriceHistory(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    asset_id: int = Field(foreign_key="asset.id")
    asset: Asset = Relationship()
    date: date
    price: float

