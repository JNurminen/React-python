from flask import Flask, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

app = Flask(__name__) # luodaan Flask  sovellus
CORS(app) # lisätään CORS sovellukseen

app.config['SQLALCHEMY_DATABASE_URI'] =  os.getenv('DATABASE_URL', 'sqlite:///friends.db') # luo tietokannan friends.db
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # estää turhat SQL kyselyt

db = SQLAlchemy(app) # luodaan SQLAlchemy tietokanta

frontend_folder = os.path.join(os.getcwd(),"..","frontend")
dist_folder = os.path.join(frontend_folder,"dist")

# Server static files from the "dist" folder under the "frontend" directory
@app.route("/",defaults={"filename":""})
@app.route("/<path:filename>")
def index(filename):
  if not filename:
    filename = "index.html"
  return send_from_directory(dist_folder,filename)

import routes

#if __name__ == "__main__":
    #with app.app_context():
        #db.create_all()

    #app.run(host='0.0.0.0', port=5000, debug=True)