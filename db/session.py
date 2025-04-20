from typing import Annotated

from fastapi import Depends
from sqlalchemy import create_engine
from sqlmodel import SQLModel, Session

# MySQL connection details
mysqldb_host = "localhost"
mysqldb_port = "3307"
mysqldb_user = "root"
mysqldb_password = "abc123"
mysqldb_database = "portfolio"

# Construct the MySQL connection URL
mysqldb_url = f"mysql+pymysql://{mysqldb_user}:{mysqldb_password}@{mysqldb_host}:{mysqldb_port}/{mysqldb_database}"

# Create the SQLAlchemy engine for MySQL
engine = create_engine(mysqldb_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]