from app import db

# Luodaan tietokantataulu Friend
class Friend(db.Model):
    id = db.Column(db.Integer, primary_key=True) # id on pääavain
    name = db.Column(db.String(100), nullable=False) # nimi ei voi olla tyhjä
    role = db.Column(db.String(50), nullable=False) # rooli ei voi olla tyhjä
    description = db.Column(db.Text, nullable=False) # kuvaus ei voi olla tyhjä
    email = db.Column(db.String(10), nullable=False) # sukupuoli ei voi olla tyhjä

    # Luodaan metodi joka palauttaa Friend taulun tiedot JSON muodossa
    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'role': self.role,
            'description': self.description,
            'email': self.email,
        }
