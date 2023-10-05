from sqlalchemy.orm import declarative_base
from sqlalchemy import VARCHAR, INTEGER, Column

Base = declarative_base()


class Objects(Base):
    __tablename__ = 'endpoint_objects'
    id = Column(VARCHAR(25), primary_key=True)
    name = Column(VARCHAR(25))
    price = Column(INTEGER)
    color = Column(VARCHAR(25))