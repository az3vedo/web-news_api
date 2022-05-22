from flask import Flask
from services.noticias import Noticias

app = Flask(__name__)

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

@app.route('/noticias/<id>/', methods=["GET"])
def find_noticias(id):
    return Noticias.findById(id)