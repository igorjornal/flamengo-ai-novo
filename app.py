from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///noticias.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class NoticiaOriginal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(200))
    texto_original = db.Column(db.Text)
    link = db.Column(db.String(200))
    fonte = db.Column(db.String(100))
    data_cadastro = db.Column(db.DateTime, default=datetime.now)

class NoticiaReescrita(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    id_original = db.Column(db.Integer)
    titulo = db.Column(db.String(200))
    texto_reescrito = db.Column(db.Text)
    tom = db.Column(db.String(50))
    posicionamento = db.Column(db.String(200))
    data_reescrita = db.Column(db.DateTime, default=datetime.now)

@app.route('/')
def home():
    return "Backend do Flamengo AI Novo está funcionando!"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=int(os.getenv('PORT', 10000)))
