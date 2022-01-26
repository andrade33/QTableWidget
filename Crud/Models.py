# coding=utf-8

from sqlalchemy import Column, String, Integer
from sqlalchemy.dialects.mysql import BLOB

from Crud.core import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///dados_A_B.db', echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()



# tabela Cliente
class Dados(Base):
    __tablename__ = 'dados'
    id = Column(Integer, primary_key=True)
    a = Column(String(40), index=True)
    b = Column(String(40))


    def __repr__(self):
        return self.a


Base.metadata.create_all(engine)