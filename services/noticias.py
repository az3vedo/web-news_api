from contextlib import closing
from db.engine import db_session
from db.db import Noticia, Autor, Assunto
from flask import jsonify

class Noticias:
  def findAll():
    with closing(db_session):
      query = db_session.query(Noticia.id, Noticia.titulo, Noticia.conteudo, Autor.nome, Assunto.nome, ).join(Autor, Assunto).all()
      header = ["id","titulo","autor","assunto"]
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