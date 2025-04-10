from typing import Annotated

from fastapi import Depends
from sqlalchemy import create_engine
from sqlmodel import SQLModel, Session

# MariaDB connection details
mariadb_host = "localhost"
mariadb_port = "3307"
mariadb_user = "root"
mariadb_password = "abc123"
mariadb_database = "portfolio"

# Construct the MariaDB connection URL
mariadb_url = f"mysql+pymysql://{mariadb_user}:{mariadb_password}@{mariadb_host}:{mariadb_port}/{mariadb_database}"

# Create the SQLAlchemy engine for MariaDB
engine = create_engine(mariadb_url)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]