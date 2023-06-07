    """Dans ce modèle de données, nous avons les entités suivantes :

    Developer : Représente un développeur, associé à un utilisateur via une relation OneToOne. Il a une bio et peut avoir plusieurs compétences liées.
    Skill : Représente une compétence, ayant simplement un nom.
    Project : Représente un projet, avec un titre, une description et une relation ForeignKey avec le développeur responsable du projet.
    Portfolio : Représente le portfolio d'un développeur, lié à un seul développeur via une relation OneToOne. Il peut contenir plusieurs projets liés et une image de couverture.

Cela vous donne une structure de données de base pour la gestion du portfolio des développeurs dans votre application Django. Vous pouvez bien sûr ajouter d'autres champs ou relations en fonction des besoins spécifiques de votre projet.
    """


from django.db import models
from django.contrib.auth.models import User

class Developer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    skills = models.ManyToManyField('Skill', blank=True)

class Skill(models.Model):
    name = models.CharField(max_length=100)

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE, related_name='projects')

class Portfolio(models.Model):
    developer = models.OneToOneField(Developer, on_delete=models.CASCADE)
    projects = models.ManyToManyField(Project, blank=True)
    cover_image = models.ImageField(upload_to='portfolio_covers/', blank=True)
