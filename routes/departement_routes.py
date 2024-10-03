# Routes pour Département
from flask import Blueprint, jsonify, request
from models import db, Departement
from app import db


bp = Blueprint('departement_routes', __name__)


@bp.route('/', methods=['GET'])
def get_departements():
    departements = Departement.query.all()
    return jsonify([{'id': d.id, 'name': d.name, 'description': d.description, 'localisation': d.localisation} for d in departements])


@bp.route('/', methods=['POST'])
def create_departement():
    data = request.get_json()
    new_departement = Departement(name=data['name'], description=data.get('description'),  localisation=data.get('localisation'))
    db.session.add(new_departement)
    db.session.commit()
    return jsonify({'message': 'Departement créé avec succès!'}), 201


@bp.route('/<int:id>', methods=['PUT'])
def update_departement(id): 
    data = request.get_json()
    departement = Departement.query.get_or_404(id)

    departement.name = data.get('name', departement.name)
    departement.description = data.get('description', departement.description)

    db.session.commit()
    return jsonify({'message': 'Département mis à jour avec succès!'})


@bp.route('/<int:id>', methods=['DELETE'])
def delete_departement(id):
    departement = Departement.query.get_or_404(id)

    db.session.delete(departement)
    db.session.commit()
    return jsonify({'message': 'Département supprimé avec succès!'})