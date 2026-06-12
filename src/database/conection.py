from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db = create_engine("sqlite:///data/app.db")
Session = sessionmaker(bind=db)
session = Session()
