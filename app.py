from flask import Flask
from services.noticias import Noticias
from services.assuntos import Assuntos

app = Flask(__name__)

@app.route('/status/')
def health_check():
    return "app is running"

@app.route('/noticias/', methods=["GET"])
def list_noticias():
    return Noticias.findAll()

@app.route('/noticias/<id>/', methods=["GET"])
def find_noticias(id):
    return Noticias.findById(id)

@app.route('/assuntos/', methods=["GET"])
def list_assuntos():
    return Assuntos.findAll()

@app.route('/noticias/assuntos/<id>', methods=["GET"])
def find_noticias_by_assunto(id):
    return Noticias.findByAssunto(id)