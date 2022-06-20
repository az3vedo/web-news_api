from contextlib import closing
from database.engine import db_session
from database.db import  Autor
from flask import jsonify

class Autores:
  def findAll():
    with closing(db_session):
      query = db_session.query(Autor.id, Autor.nome).all()
      header = ["id", "autor"]
      response = []
      for result in query:
        response.append(dict(zip(header,result)))
      return jsonify(response)

  def addAutor(request):
    with closing(db_session):
      autor = Autor(
      nome=request['nome'])
      db_session.add(autor)
      db_session.commit()
    return({"message": "autor criado"})