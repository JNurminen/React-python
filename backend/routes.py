from app import app, db
from flask import request, jsonify
from models import Friend

# haetaan kaikki ystävät
@app.route('/api/friends', methods=['GET'])
def get_friends():
    friends = Friend.query.all() # haetaan kaikki ystävät
    json_friends = list(map(lambda x: x.to_jason(), friends)) # lista johon ystävät tallennetaan
    return jsonify({"friends":json_friends}),200 # palautetaan ystävät JSON muodossa


# luodaan uusi ystävä
@app.route('/friends', methods=['POST'])
def create_friend():
    try:
        data = request.get_json() # haetaan pyynnön mukana tuleva data

        # tarkistetaan että kaikki pakolliset kentät ovat datassa
        required_fields = ['name', 'role', 'description', 'email'] # pakolliset kentät
        for field in required_fields:
            if field not in data: # jos pakollista kenttää ei ole datassa
                return jsonify({"Error": f"Missing required field: {field} is required"}),400 # palautetaan virheilmoitus

        name = data.get('name') # haetaan nimi datasta
        role = data.get('role') # haetaan rooli datasta
        description = data.get('description') # haetaan kuvaus data
        email = data.get('email') # haetaan sukupuoli datasta

        # luodaan uusi ystävä
        new_friend = Friend(name=name, role=role, description=description, email=email)

        db.session.add(new_friend) # lisätään uusi ystävä tietokantaan
        db.session.commit() # tallennetaan muutokset tietokantaan
        return jsonify({"msg":"Friend created succesfully"}),201 # palautetaan luotu ystävä JSON muodossa
    
    # virheenkäsittely
    except Exception as e:
        db.session.rollback() # perutaan muutokset tietokantaan
        return jsonify({"Error": str(e)}),500 # palautetaan virheilmoitus

# poistetaan ystävä
@app.route('/friends/<int:id>', methods=['DELETE'])
def delete_friend(id):
    try:
        friend = Friend.query.get(id) # haetaan ystävä id:n perusteella
        if friend is None: # jos ystävää ei löydy
            return jsonify({"Error": "Friend not found"}),404 # palautetaan virheilmoitus
    
        db.session.delete(friend) # poistetaan ystävä tietokannasta
        db.session.commit() # tallennetaan muutokset tietokantaan
        return jsonify({"msg":"Friend deleted succesfully"}),200 # palautetaan onnistumisviesti
    
    except Exception as e:
        db.session.rollback() # perutaan muutokset tietokantaan
        return jsonify({"Error": str(e)}),500 # palautetaan virheilmoitus
          
# päivitetään ystävän tiedot
@app.route('/friends/<int:id>', methods=['PUT'])
def update_friend(id):
    try:
        friend = Friend.query.get(id) # haetaan ystävä id:n perusteella
        if friend is None: # jos ystävää ei löydy
            return jsonify({"Error": "Friend not found"}),404 # palautetaan virheilmoitus

        data = request.get_json() # haetaan pyynnön mukana tuleva data

        # päivitetään ystävän tiedot
        friend.name = data.get('name', friend.name) # päivitetään nimi
        friend.role = data.get('role', friend.role) # päivitetään rooli
        friend.description = data.get('description', friend.description) # päivitetään työnkuva
        friend.email = data.get('email', friend.email) # päivitetään sähköposti

        db.session.commit() # tallennetaan muutokset tietokantaan
        return jsonify({"msg":"Friend updated succesfully"}),200 # palautetaan onnistumisviesti

    except Exception as e:
        db.session.rollback() # perutaan muutokset tietokantaan
        return jsonify({"Error": str(e)}),500 # palautetaan virheilmoitus