## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

### Deploiement

### Prérequis

les meme prérequis que pour le developpement local sont demandé avec en plus:
  - Compte ``Sentry`` ainsi que le ``DNS`` du projet
  - Compte ``Docker Hub`` avec identifiants( username et mot de passe)
  - Compte ``Render`` avec un projet Web / ainsi que l'url du **Deploy Hook**
  - Compte ``Circle Ci``




#### *Fonctionnement du deploiement*.

Chaque commit ``pusher`` sur le repository GITHUB de l'application, va declencher le ***workflow Circle CI***.

Le workflow est une serie de `Bluid`. Voici leurs fonctions:
  * `Build_and_test` : Installe les packages de l'application, lance les tests unitaire et d'integrations. Le workflow passe au bluid suivant seulement si:
      - Le commit est réalisé sur la branche ``master``.
      - Tous les tests sont passés avec succés.
      - La couverture des tests est superieur à 80%.  

  * `Build-docker-image` :  Construction de l'``image Docker`` de l'application, redefini son tag avec le SHA du commit, et la pousse sur le repository ``Docker Hub``.
  Si toutes ses opérations sont reussi, le workflow lance build suivant.
  * ``deployment`` : Deploye le nouveau commit sur Render.


**_Configuration Render:_**

Dans votre ``projet web Render`` vous devez ajouter, dans `Environment`, les variables d'environnement suivantes:
 - `SENTRY_DNS` = **_votre dns sentry du projet_**
 - `SECRET_KEY_DJANGO` = **_votre clé secret Django_**

Dans settings veillez a bien recuperer la cle `Deploy Hook`.

**_Configuration Cercle CI:_**

Dans votre projet Cercle CI, une fois votre projet lié a votre repository GITHUB de l'applications, vous devez égalment configurez les variables d'environnements dans `Project Settings`:

 - `SENTRY_DNS` = **_votre dns sentry du projet_**
 - `SECRET_KEY_DJANGO` = **_votre clé secret Django_**
 - `DOCKERHUB_PASSWORD` = **_votre mot de passe Docker Hub_**
 - `DOCKERHUB_USERNAME` = **_votre identifiant Docker Hub_**
  - `RENDER_KEY` = la clé **_Deploy Hook de Render_**
 





