from contextlib import closing
from database.engine import db_session
from database.db import Noticia, Autor, Assunto
from flask import jsonify

class Assuntos:
  def findAll():
    with closing(db_session):
      query = db_session.query(Assunto.id, Assunto.nome).all()
      header = ["id", "assunto"]
      response = []
      for result in query:
        response.append(dict(zip(header,result)))
      return jsonify(response)
