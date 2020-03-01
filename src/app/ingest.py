from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.db import movies
from app.api.models import MovieSchema


DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

# create a configured "Session" class
Session = sessionmaker(bind=engine)

# create a Session
session = Session()

session.bulk_insert_mappings(MovieSchema, df.to_dict(orient="records"))
session.close()