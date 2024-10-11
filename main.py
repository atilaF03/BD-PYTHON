import os
from sqlalchemy import create_engine, Column ,String,Integer
from sqlalchemy.orm import sessionmaker, declarative_base
# cria 
db = create_engine("sqlite:///meubanco.db")

Session = sessionmaker(bind = db)


session = Session()

Base = declarative_base()
class Usuario(Base):
    __tablename__= "usuarios"
    id = Column("id", Integer,primary_key =True, autoincrement=True)
    nome= Column("nome",String)
    email = Column("email",String)
    senha = Column("senha",String)


    def __init__(self,nome:str, email:str,senha:str) -> None:
        self.nome= nome
        self.email = email
        self.senha = senha

Base.metadata.create_all(bind=db)
os.system("cls||clear")
        
for i in range(1):
    nome= input("Digite seu nome: ")
    email = input("Digite seu e-mail: ")
    senha= input("Digite sua senha: ")
    os.system("cls||clear")
    usuario = Usuario( nome= nome,email = email,senha=senha)
    session.add(usuario)
    session.commit()

lista_usuarios = session.query(Usuario).all()

for usuario in lista_usuarios:
    print(f"{usuario.id}- {usuario.nome}-{usuario.email}-{usuario.senha}")