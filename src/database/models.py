from sqlalchemy import Integer, String, Boolean, Column
from sqlalchemy.orm import declarative_base
from src.database.conection import db


Base = declarative_base()


class Usuario(Base):
    __tablename__ = "usuarios"
    id = Column("id", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String, nullable=False)
    senha = Column("senha", String, nullable=False)
    email = Column("email", String, unique=True, nullable=False)
    admin = Column("admin", Boolean)

    def __init__(self, nome, senha, email, admin=False):
        self.nome = nome
        self.senha = senha
        self.email = email
        self.admin = admin


Base.metadata.create_all(bind=db)
