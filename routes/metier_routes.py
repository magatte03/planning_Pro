# Routes pour Métier
from flask import Blueprint, jsonify, request
from models import db, Metier
from app import db


bp = Blueprint('metier_routes', __name__)


@bp.route('/', methods=['GET'])
def get_metiers():
    metiers = Metier.query.all()
    return jsonify([{'id': m.id, 'code': m.code,'nom': m.nom ,'description': m.description, 'departement_id': m.departement_id} for m in metiers])


@bp.route('/', methods=['POST'])
def create_metier():
    data = request.get_json()
    new_metier = Metier(code=data['code'], nom=data.get('nom'), description=data.get('description'), departement_id=data['departement_id'])
    db.session.add(new_metier)
    db.session.commit()
    return jsonify({'message': 'Métier créé avec succès!'}), 201


@bp.route('/<int:id>', methods=['PUT'])
def update_metier(id):
    data = request.get_json()
    metier = Metier.query.get_or_404(id)

    metier.code = data.get('code', metier.code)
    metier.nom = data.get('nom', metier.nom)
    metier.description = data.get('description', metier.description)
    metier.departement_id = data.get('departement_id', metier.departement_id)

    db.session.commit()
    return jsonify({'message': 'Métier mis à jour avec succès!'})
    
    
@bp.route('/<int:id>', methods=['DELETE'])
def delete_metier(id):
    metier = Metier.query.get_or_404(id)

    db.session.delete(metier)
    db.session.commit()
    return jsonify({'message': 'Métier supprimé avec succès!'})
        