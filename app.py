# C'est le fichier principal pour démarrer l'application Flask.
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_cors import CORS
from config import Config


# Initialisation de Flask et des extensions
app = Flask(__name__)

# Configuration de la base de données
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:12345678@localhost/planning_pro_bd'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
CORS(app)


# Import des blueprints
from routes.metier_routes import bp as metier_bp
from routes.departement_routes import bp as departement_bp

app.register_blueprint(metier_bp, url_prefix='/api/metiers')
app.register_blueprint(departement_bp, url_prefix='/api/departements')

if __name__ == '__main__':
    app.run(debug=True)
