# Modèle pour le Département
from app import db

class Departement(db.Model):
    __tablename__ = 'departements'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=True)
    description = db.Column(db.String(255), nullable=True)
    localisation = db.Column(db.String(255), nullable=True)

    # Relation de composition avec Metier
    metiers = db.relationship('Metier', backref='departement', lazy=True)

    def __repr__(self):
        return f'<Departement {self.nom}>'