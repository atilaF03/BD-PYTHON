import os
from sqlalchemy import create_engine, column ,String,Integer
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine("sqllite:///meubanco.db")

Session = sessionmaker(bin = db)

session = Session()



Base = declarative_base()
class Usuario(Base):
    __tablename__= "usuarios"

    id = column("id",Integer, primary_key =True,autoincrement=True)
    nome=column("nome",String)
    email = column("email",String)
    senha = column("senha",String)


    def __init__(self,nome:str, email:str,senha:str) -> None:
        self.nome= nome
        self.email = email
        self.senha = senha

Base.metadata.create_all(bin=db)
        
