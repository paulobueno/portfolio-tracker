import os
from typing import Annotated

from fastapi import Depends
from sqlalchemy import create_engine
from sqlmodel import SQLModel, Session

# MySQL connection details
mysqldb_host = os.getenv("MYSQL_HOST")
mysqldb_port = os.getenv("MYSQL_PORT")
mysqldb_user = os.getenv("MYSQL_USER")
mysqldb_password = os.getenv("MYSQL_PASSWORD")
mysqldb_database = os.getenv("MYSQL_DATABASE")

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