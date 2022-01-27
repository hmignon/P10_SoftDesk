# Projet 10 DA-Python OC (Hélène Mignon)

***Livrable du Projet 10 du parcours D-A Python d'OpenClassrooms***

API-SoftDesk est une API RESTful permettant de remonter et suivre des problèmes 
techniques pour les trois plateformes (site web, applications Android et iOS).

L'application permet aux utilisateurs de créer divers projets, 
d'ajouter des utilisateurs (contributeurs) à des projets spécifiques, 
de créer des problèmes au sein des projets et d'attribuer des libellés 
à ces problèmes en fonction de leurs priorités, de balises, etc.

Pour plus de détails sur le fonctionnement de cette API, se référer à sa 
[documentation](https://documenter.getpostman.com/view/19098124/UVe9SpoZ) (Postman).

_Testé sous Windows 10 - Python 3.9.5 - Django 4.0.1 - DRF 3.13.1_

## Initialisation du projet

### Windows :
Dans Windows Powershell, naviguer vers le dossier souhaité.
###### • Récupération du projet

```
git clone https://github.com/hmignon/P10_mignon_helene.git
```

###### • Activer l'environnement virtuel

```
cd P10_mignon_helene 
python -m venv env 
env\Scripts\activate
```

###### • Installer les paquets requis

```
pip install -r requirements.txt
```


### MacOS et Linux :
Dans le terminal, naviguer vers le dossier souhaité.
###### • Récupération du projet
```
git clone https://github.com/hmignon/P10_mignon_helene.git
```

###### • Activer l'environnement virtuel
```
cd P10_mignon_helene 
python3 -m venv env 
source env/bin/activate
```

###### • Installer les paquets requis
```
pip install -r requirements.txt
```

## Utilisation

#### Faire les migrations (si nécessaire) :

```
python manage.py migrate
```

#### Lancer le serveur Django :

```
python manage.py runserver
```

Il est possible de naviguer dans l'API avec différents outils :

- la plateforme [Postman](https://www.postman.com/) ;
- l'outil de commandes [cURL](https://curl.se) ;
- l'interface intégrée Django REST framework à l'adresse http://127.0.0.1:8000/ (adresse par défaut, cf. points de terminaison ci-dessous).

## Informations

#### Liste des utilisateurs existants :

| *ID* | *Identifiant* | *Mot de passe* |
|------|---------------|----------------|
| 1    | testuser      | password321    |
| 3    | user_2        | password321    |
| 4    | new_user      | password321    |


#### Liste des points de terminaison de l'API (détaillés dans la [documentation](https://documenter.getpostman.com/view/19098124/UVe9SpoZ)) :

| #   | *Point de terminaison d'API*                                              | *Méthode HTTP* | *URL (base: http://127.0.0.1:8000)*       |
|-----|---------------------------------------------------------------------------|----------------|-------------------------------------------|
| 1   | Inscription de l'utilisateur                                              | POST           | /signup/                                  |
| 2   | Connexion de l'utilisateur                                                | POST           | /login/                                   |
| 3   | Récupérer la liste de tous les projets rattachés à l'utilisateur connecté | GET            | /projects/                                |
| 4   | Créer un projet                                                           | POST           | /projects/                                |
| 5   | Récupérer les détails d'un projet via son id                              | GET            | /projects/{id}/                           |
| 6   | Mettre à jour un projet                                                   | PUT            | /projects/{id}/                           |
| 7   | Supprimer un projet et ses problèmes                                      | DELETE         | /projects/{id}/                           |
| 8   | Ajouter un utilisateur (collaborateur) à un projet                        | POST           | /projects/{id}/users/                     |
| 9   | Récupérer la liste de tous les utilisateurs attachés à un projet          | GET            | /projects/{id}/users/                     |
| 10  | Supprimer un utilisateur d'un projet                                      | DELETE         | /projects/{id}/users/{id}/                |
| 11  | Récupérer la liste des problèmes liés à un projet                         | GET            | /projects/{id}/issues/                    |
| 12  | Créer un problème dans un projet                                          | POST           | /projects/{id}/issues/                    |
| 13  | Mettre à jour un problème dans un projet                                  | PUT            | /projects/{id}/issues/{id}/               |
| 14  | Supprimer un problème d'un projet                                         | DELETE         | /projects/{id}/issues/{id}/               |
| 15  | Créer des commentaires sur un problème                                    | POST           | /projects/{id}/issues/{id}/comments/      |
| 16  | Récupérer la liste de tous les commentaires liés à un problème            | GET            | /projects/{id}/issues/{id}/comments/      |
| 17  | Modifier un commentaire                                                   | PUT            | /projects/{id}/issues/{id}/comments/{id}/ |
| 18  | Supprimer un commentaire                                                  | DELETE         | /projects/{id}/issues/{id}/comments/{id}/ |
| 19  | Récupérer un commentaire via son id                                       | GET            | /projects/{id}/issues/{id}/comments/{id}/ |