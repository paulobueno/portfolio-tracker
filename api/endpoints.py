from sqlmodel import select
from db.session import SessionDep
from models.models import Asset, AssetCategory, Transaction
from serializers.serializers import AssetOut, AssetCreate, AssetCategoryOut, AssetCategoryCreate, TransactionCreate, TransactionOut
from fastapi import APIRouter

router = APIRouter()

@router.get("/asset/")
async def list_assets(session: SessionDep) -> list[AssetOut]:
    stmt = select(Asset)
    assets = session.exec(stmt).all()
    return assets


@router.post("/asset/")
async def create_asset(asset: AssetCreate, session: SessionDep) -> AssetOut:
    db_asset = Asset.model_validate(asset)
    session.add(db_asset)
    session.commit()
    session.refresh(db_asset)
    return db_asset


@router.get("/asset-category/")
async def list_asset_categories(session: SessionDep) -> list[AssetCategoryOut]:
    asset_category = session.exec(select(AssetCategory)).all()
    return asset_category


@router.post("/asset-category/")
async def create_asset_category(asset_category: AssetCategoryCreate, session: SessionDep) -> AssetCategoryOut:
    db_asset_category = AssetCategory.model_validate(asset_category)
    session.add(db_asset_category)
    session.commit()
    session.refresh(db_asset_category)
    return db_asset_category


@router.get("/transaction/")
async def list_transactions(session: SessionDep):
    stmt = select(Transaction)
    transactions = session.exec(stmt).all()
    return transactions

@router.post("/transaction/")
async def create_transaction(transaction: TransactionCreate, session: SessionDep) -> TransactionOut:
    db_transaction = Transaction.model_validate(transaction)
    session.add(db_transaction)
    session.commit()
    session.refresh(db_transaction)
    return db_transaction

