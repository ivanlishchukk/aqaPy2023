from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session


engine = create_engine("postgresql://postgres:05071998qaz@localhost:5432/postgres")

__session = sessionmaker(engine)
session: Session = __session()