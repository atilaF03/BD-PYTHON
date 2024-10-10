import os
from sqlalchemy import create_engine, column ,String,Integer
from sqlalchemy.orm import sessionmaker, declarative_base

db = create_engine("sqlite:///meubanco.db")

Session = sessionmaker(bind = db)

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

Base.metadata.create_all(bind=db)
        
usuario = Usuario("marta", "marta@gmail.com","123")
session.add(usuario)
session.commit()

lista_usuarios= session.query(Usuario).all()

for usuario in lista_usuarios:
    print(f"{usuario.id}- {usuario.nome}-{usuario.email}")