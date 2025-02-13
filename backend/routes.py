from app import app, db
from flask import request, jsonify
from models import Friend

# haetaan kaikki ystävät
@app.route("/api/friends", methods=['GET'])
def get_friends():
    friends = Friend.query.all() # haetaan kaikki ystävät
    json_friends = list(map(lambda x: x.to_json(), friends)) # lista johon ystävät tallennetaan
    return jsonify({"friends": json_friends}), 200 # palautetaan ystävät JSON muodossa

# luodaan uusi ystävä
@app.route("/create_friend", methods=['POST'])
def create_friend():
    name = request.json.get('name') # haetaan nimi
    role = request.json.get('role') # haetaan rooli
    description = request.json.get('description') # haetaan työnkuva
    gender = request.json.get('gender') # haetaan sukupuoli

    if not name or not role or not description or not gender: # jos jokin tieto puuttuu
        return jsonify({"message": "Please provide all information"}), 400 # palautetaan virheilmoitus
    
    new_friend = Friend(name=name, role=role, description=description, gender=gender) # luodaan uusi ystävä
    try:
        db.session.add(new_friend) # lisätään uusi ystävä tietokantaan
        db.session.commit() # tallennetaan muutokset tietokantaan
    except Exception as e:
        return jsonify({"message": str(e)}), 400 # palautetaan virheilmoitus
    
    return jsonify({"message": "Friend created successfully"}), 201 # palautetaan onnistumisviesti

# poistetaan ystävä
@app.route('/delete_friend/<int:id>', methods=['DELETE'])
def delete_friend(id):
    friend = Friend.query.get(id) # haetaan ystävä id:n perusteella

    if not friend: # jos ystävää ei löydy
        return jsonify({"message": "Friend not found"}), 404 # palautetaan virheilmoitus
    
    db.session.delete(friend) # poistetaan ystävä tietokannasta
    db.session.commit() # tallennetaan muutokset tietokantaan

    return jsonify({"message": "Friend deleted successfully"}), 200 # palautetaan onnistumisviesti

# päivitetään ystävän tiedot
@app.route("/update_friend/<int:id>", methods=['PATCH'])
def update_friend(id):
    friend = Friend.query.get(id) # haetaan ystävä id:n perusteella

    if not friend: # jos ystävää ei löydy
        return jsonify({"message": "Friend not found"}), 404 # palautetaan virheilmoitus

    data = request.json # haetaan pyynnön mukana tuleva data

    # päivitetään ystävän tiedot
    friend.name = data.get('name', friend.name) # päivitetään nimi
    friend.role = data.get('role', friend.role) # päivitetään rooli
    friend.description = data.get('description', friend.description) # päivitetään työnkuva
    friend.gender = data.get('gender', friend.gender) # päivitetään sukupuoli

    db.session.commit() # tallennetaan muutokset tietokantaan
    return jsonify({"message": "Friend updated successfully"}), 200 # palautetaan onnistumisviesti

#import routes

#if __name__ == "__main__":
    #with app.app_context():
        #db.create_all()

    #app.run(host='0.0.0.0', port=5000, debug=True) # käynnistetään sovellus debug tilassa