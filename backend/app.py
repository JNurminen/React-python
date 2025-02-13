from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__) # luodaan Flask  sovellus
CORS(app) # lisätään CORS sovellukseen

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///friends.db' # luo tietokannan friends.db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # estää turhat SQL kyselyt

db = SQLAlchemy(app) # luodaan SQLAlchemy tietokanta

frontend_folder = os.path.join(os.getcwd(), '..', 'frontend') # määritetään frontend kansio
dist_folder = os.path.join(frontend_folder, 'dist') # määritetään dist kansio

@app.route('/', defaults={'filename': ''}) # määritetään juuri polku
@app.route('/<path:filename>') # määritetään polku
def index(filename): # luodaan index funktio
    if not filename:
        filename = 'index.html' # määritetään index.html
    return send_from_directory(dist_folder, filename) # palautetaan tiedosto

