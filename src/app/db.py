import os

from sqlalchemy import (Column, DateTime, Integer, MetaData, String, Text, Table,
                        create_engine)
from sqlalchemy.sql import func

from databases import Database

DATABASE_URL = os.getenv("DATABASE_URL")

# SQLAlchemy
engine = create_engine(DATABASE_URL)
metadata = MetaData()

movies = Table(
    "movies",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("release_year", String()),
    Column("title", String()),
    Column("origin_ethnicity", String()),
    Column("director", String()),
    Column("cast", String()),
    Column("genre", String()),
    Column("wiki_page", String()),
    Column("plot", Text()),
    Column("created_date", DateTime, default=func.now(), nullable=False),
)

# databases query builder
database = Database(DATABASE_URL)