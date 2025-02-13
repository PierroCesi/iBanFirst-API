# iBanFirst API

API REST pour gérer les comptes bancaires avec support de conversion de devises.

## Description

Cette API permet de :
- Récupérer les comptes par propriétaire
- Convertir les montants des comptesdans différentes devises

## Technologies

- Langage : Python 3.10
- Framework : Flask
- Serveur : Gunicorn
- Container : Docker

---

## Installation

### Prérequis
- Python 3.10+
- Docker (pour la production uniquement)
- Clé API Forex Rate (https://forexrateapi.com)

### Configuration initiale
1. Créer le fichier `.env` à la racine du projet à partir de `.env.example`
2. Remplacer la clé API Forex Rate dans le fichier `.env` et `.env.production`

Un bon fichier de configuration devrait ressembler à ceci :
```
FLASK_APP=wsgi.py
FLASK_ENV=development
FOREX_API_KEY=your_api_key_here
```

---

## Développement local

1. Créer un environnement virtuel :

```sh
python -m venv venv
source venv/bin/activate      # Linux/MacOS
venv\Scripts\activate         # Windows
```

2. Installer les dépendances :

```sh
pip install -r requirements.txt
```

3. Lancer le serveur de développement :

```sh
flask run
```

L'API sera accessible sur http://localhost:5000

---

## Production avec Docker

S'assurer que le fichier `.env.production` est correctement configuré. Cf [Configuration initiale](#configuration-initiale)

### Construction de l'image
```sh
make build
```

### Démarrage du conteneur
```sh
make run
```

### Autres commandes utiles
```sh
make build-no-cache    # Build sans cache
make stop              # Arrêter le conteneur
make clean             # Supprimer le conteneur
make logs              # Voir les logs
make bash              # Ouvrir un terminal dans le conteneur
```

---

## Documentation API

### Endpoints disponibles

- GET /api/v1/accounts/<owner_id>
- GET /api/v1/accounts/<owner_id>?currency=ANY_CURRENCY 

## Tests

Pour exécuter les tests :
```sh
pytest
```