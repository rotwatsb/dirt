from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    def __repr__(self):
        return "<User(id=%s name='%s')>" % (
            self.id,
            self.name
        )
