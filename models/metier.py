# Modèle pour le Métier
from app import db

class Metier(db.Model):
    __tablename__ = 'metiers'

    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(25), nullable=True)
    nom = db.Column(db.String(255), nullable=True)
    description = db.Column(db.String(255), nullable=True)

    # Clé étrangère pointant vers Departement
    departement_id = db.Column(db.Integer, db.ForeignKey('departements.id'), nullable=False)

    def __repr__(self):
        return f'<Metier {self.nom}>'
    