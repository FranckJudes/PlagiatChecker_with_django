
# PlagiatChecker with Django

**PlagiatChecker** est une application web développée en Python utilisant le framework Django, conçue pour détecter le plagiat dans des documents.

## Fonctionnalités Principales

- **Téléversement de Documents** : Les utilisateurs peuvent téléverser des documents pour analyse.

- **Détection de Plagiat** : L'application analyse les documents téléversés pour identifier des similitudes avec des sources existantes, détectant ainsi des cas potentiels de plagiat.

- **Système de Scoring** : Elle génère des scores de similarité pour quantifier l'originalité des documents.

- **Présentation des Résultats** : Les résultats détaillés sont présentés, indiquant les pourcentages de similarité et les sections concernées.

## Technologies Utilisées

- **Backend** : Django (Python)

- **Frontend** : HTML, CSS, JavaScript

- **Base de Données** : SQLite (par défaut avec Django)

## Installation et Exécution

Pour exécuter l'application localement :

1. **Cloner le dépôt** :
   ```bash
   git clone https://github.com/FranckJudes/PlagiatChecker_with_django.git
   ```

2. **Naviguer vers le répertoire du projet** :
   ```bash
   cd PlagiatChecker_with_django/PlagiatChecker
   ```

3. **Activer l'environnement virtuel** :
   ```bash
   source .env/bin/activate
   ```

4. **Installer les dépendances** :
   ```bash
   pip install -r requirements.txt
   ```

5. **Appliquer les migrations** :
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Lancer le serveur de développement** :
   ```bash
   python manage.py runserver
   ```


