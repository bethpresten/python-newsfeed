from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()

# connect to database using env variable
engine = create_engine("mysql+pymysql://root:PASSWORD@localhost/python_news_db")
Session = sessionmaker(bind=engine)
Base = declarative_base()