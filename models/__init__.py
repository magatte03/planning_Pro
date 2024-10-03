# models/__init__.py
from flask_sqlalchemy import SQLAlchemy

# Initialisation de SQLAlchemy
db = SQLAlchemy()

# Importation des modèles
from .departement import Departement
from .metier import Metier
