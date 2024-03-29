from contextlib import closing
from database.engine import db_session
from database.db import Assunto
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

  def addAssunto(request):
    with closing(db_session):
      assunto = Assunto(
      nome=request['nome'])
      db_session.add(assunto)
      db_session.commit()
    return({"message": "Assunto criado"})