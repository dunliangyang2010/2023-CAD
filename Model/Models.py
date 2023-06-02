from sqlalchemy import Column, Integer, String, JSON, Numeric, Text
from . import Database

class User(Database.UserBase().base()):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    name = Column(String(200))
    raw = Column(JSON)
    result = Column(JSON)
    probability = Column(Numeric)
    tag = Column(Text)

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, raw={self.raw}, result={self.raw}, probability={self.probability}, tag={self.tag})"