from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm.session import Session


engine = create_engine('sqlite:///worklog.db', )
db_session = sessionmaker(bind=engine)
session = Session(bind=engine)
Base = declarative_base()