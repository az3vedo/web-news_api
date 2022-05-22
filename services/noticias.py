from contextlib import closing
from database.engine import db_session
from database.db import Noticia, Autor, Assunto
from flask import jsonify

class Noticias:
  def findAll():
    with closing(db_session):
      query = db_session.query(Noticia.id, Noticia.titulo, Noticia.conteudo, Autor.nome, Assunto.nome).join(Autor, Assunto).all()
      header = ["id","titulo", "conteudo", "autor","assunto"]
      response = []
      for result in query:
        # text = "id: {},titulo: {},conteudo: {},autor: {},assunto: {}".format(result[0], result[1], result[2], result[3], result[4])
        response.append(dict(zip(header, result)))
      return jsonify(response)
  
  def findById(id):
    with closing(db_session):
      query = db_session.query(Noticia.titulo, Noticia.conteudo, Autor.nome, Assunto.nome).filter_by(id = id).join(Autor, Assunto).all()
      header = ["titulo", "conteudo", "autor", "assunto"]
      response = []
      for result in query:
        response.append(dict(zip(header,result)))
      return jsonify(response)
  
  def seed_db():
    with closing(db_session):
      autor = Autor(nome='Gabriel')
      assunto1 = Assunto(nome='Esportes')
      assunto2 = Assunto(nome='Astronomia')
      n1 = Noticia(conteudo='Foi descoberta uma nova estrela', titulo='Brilha-brilha', id_autor=1, id_assunto=2)
      n2 = Noticia(conteudo='Time perde grande patrocínio após se enolver em polêmica', titulo='Bola fora', id_autor=1, id_assunto=1)
      n3 = Noticia(conteudo='natação tem grande destaque nas olimpíadas', titulo='Nadando com a maré', id_autor=1, id_assunto=1)
      n4 = Noticia(conteudo='Gramados de grandes jogos passarão a ser azuis no mês de novembro em campanha', titulo='Futbol azul', id_autor=1, id_assunto=1)
      db_session.add(autor)
      db_session.add(assunto1)
      db_session.add(assunto2)
      db_session.add(n1)
      db_session.add(n2)
      db_session.add(n3)
      db_session.add(n4)
      db_session.commit()
