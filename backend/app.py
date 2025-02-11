from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__) # luodaan Flask  sovellus
CORS(app) # lisätään CORS sovellukseen

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///friends.db' # luo tietokannan friends.db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # estää turhat SQL kyselyt

db = SQLAlchemy(app) # luodaan SQLAlchemy tietokanta


#import routes # tuodaan routes.py tiedosto

#with app.app_context():
    #db.create_all() # luodaan tietokantataulut

#if __name__ == '__main__':
    #app.run(debug=True) # käynnistetään sovellus debug tilassa