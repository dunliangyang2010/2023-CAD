from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv
import os
load_dotenv()

user = os.getenv("USER")
password = os.getenv("PASSWORD")
db_ip = os.getenv("DB_IP")
db_port = os.getenv("DB_PORT")
db_name = os.getenv("DATABASE")

engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{db_ip}:{db_port}/{db_name}')
metadata = MetaData()

class UserBase(object):
    def __init__(self):
        self.table = Table('user', metadata, autoload_with=engine)
    def session(self):
        session_object = sessionmaker(bind=engine)
        session = session_object()
        return session
    def base(self):
        user_base = declarative_base()
        return user_base