from flask import Flask, request
from flask_cors import CORS, cross_origin
from services.noticias import Noticias
from services.assuntos import Assuntos
from services.autores import Autores

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/')
def seed():
    Noticias.seed_db()
    return "Banco populado"

@app.route('/status/')
def health_check():
    return "app is running"

@app.route('/noticias/', methods=["GET"])
def list_noticias():
    return Noticias.findAll()

@app.route('/noticia/<id>/', methods=["GET"])
def find_noticias(id):
    return Noticias.findById(id)

@app.route('/assuntos/', methods=["GET"])
def list_assuntos():
    return Assuntos.findAll()

@app.route('/noticias/assuntos/<id>', methods=["GET"])
def find_noticias_by_assunto(id):
    return Noticias.findByAssunto(id)

@app.route('/noticias/add/', methods=["POST"])
def add_noticia():
    request_data = request.get_json()
    return Noticias.addNoticia(request_data)

@app.route('/assunto/add/', methods=["POST"])
def add_assunto():
    request_data = request.get_json()
    return Assuntos.addAssunto(request_data)

@app.route('/autor/add/', methods=["POST"])
def add_autor():
    request_data = request.get_json()
    return Autores.addAutor(request_data)

@app.route('/noticias/edit/', methods=["PUT"])
def edit_noticia():
    request_data = request.get_json()
    return Noticias.editNoticia(request_data)

@cross_origin()
@app.route('/noticias/delete/', methods=["DELETE"])
def delete_noticia():
    request_data = request.get_json()
    return Noticias.deleteNoticia(request_data)