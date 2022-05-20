from sqlalchemy import Column, ForeignKey, Integer, String, Text
from sqlalchemy.orm import declarative_base, relation
from database.engine import db_engine

Base = declarative_base()

class Autor(Base):
  __tablename__ = "autores"
  id = Column(Integer, primary_key=True)
  nome = Column(String(80))

class Assunto(Base):
  __tablename__ = "assuntos"
  id = Column(Integer, primary_key=True)
  nome = Column(String(50), nullable=False)

class Noticia(Base):
  __tablename__ = "noticias"
  id = Column(Integer, primary_key=True)
  titulo = Column(String(35), nullable=False) 
  id_assunto = Column(Integer, ForeignKey("assuntos.id"), nullable=False)
  conteudo = Column(Text, nullable=False)
  id_autor = Column(Integer, ForeignKey("autores.id"), nullable=False)

#Base.metadata.create_all(db_engine)

