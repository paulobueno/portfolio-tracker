from sqlmodel import SQLModel, Relationship, Field

class AssetCategory(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field()
    assets: list['Asset'] = Relationship(back_populates="category")

class Asset(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    name: str = Field()
    ticker: str = Field(index=True)
    description: str | None = Field(default=None)
    detail: str | None = Field(default=None)
    category_id: int | None = Field(default=None, foreign_key="assetcategory.id")
    category: AssetCategory | None = Relationship(back_populates="assets")
