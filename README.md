[![wakatime](https://wakatime.com/badge/user/648b0556-0c0e-4e9d-b952-2bea950dabe6/project/92a9cd61-f530-4875-ba3e-2a1e222b85cd.svg)](https://wakatime.com/badge/user/648b0556-0c0e-4e9d-b952-2bea950dabe6/project/92a9cd61-f530-4875-ba3e-2a1e222b85cd)
[![Codacy Badge](https://app.codacy.com/project/badge/Grade/7d8e8c6f6e264b8688dae88328f21224)](https://app.codacy.com/gh/jbbaillet85/portefolio/dashboard?utm_source=gh&utm_medium=referral&utm_content=&utm_campaign=Badge_grade)
# portefolio

application django de présentation de portefolio de développeur

Tableau Trello: <https://trello.com/b/QhUFcSLb/portefolio>

# Portefolio
En tant que développeur, je souhaite développer un portfolio en ligne en utilisant le framework Django. Ce portfolio me permettra de mettre en valeur mes compétences, mes projets et mes réalisations professionnelles de manière efficace et professionnelle. Il sera conçu pour être facilement administrable et évolutif. Ce portfolio sera une vitrine de mon travail et me permettra de mettre en avant mon expertise et mon expérience auprès des potentiels employeurs ou clients.

## Installation des dépendances back-end

Ce projet utilise l'outil pipenv pour gérer ses dépendances back-end. S'il n'est pas
déjà installé sur votre ordinateur, vous pouvez l'installer à l'aide de la commande
`pip install pipenv`.

Une fois pipenv installé, il vous suffit de suivre les instructions suivantes:
- Si vous avez décidé d'utiliser Postgresql, lancer la base de donnée à l'aide de `docker-compose up -d`
- Exécuter les migrations avec `pipenv run python manage.py migrate`
- Créer un super-utilisateur avec `pipenv run python manage.py createsuperuser`


## Installation des dépendances front-end

Pour les dépendances frontend, il est également nécessaire d'installer Node.js sur votre
ordinateur. Vous vouvez le faire en téléchargeant le binaire d'installation [directement
depuis cette page](https://nodejs.org/en/download), en l'exécutant et en suivant les
instructions. Node.js installera la commande npm qui vous permettra d'installer
les dépendances pour CSS et Javascript.

Une fois que node est installé, rendez-vous dans le sous-répertoire frontend du projet
et exécuter la commande `npm install`.

Un fois les dépendances installées, vous pouvez utiliser la commande `npm run start` pour
développer, ou `npm run build` pour compiler les fichiers de production.