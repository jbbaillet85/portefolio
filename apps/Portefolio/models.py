from django.db import models
from django.utils.translation import gettext_lazy
from django_extensions.db.fields import AutoSlugField
from config.settings.base import AUTH_USER_MODEL


class Skill(models.Model):
    name = models.CharField(max_length=100)


class Techno(models.Model):
    name = models.CharField(max_length=256)


class Developer(models.Model):
    name = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    skills = models.ManyToManyField('Skill', blank=True)


class Project(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    techno = models.ManyToManyField(Techno, blank=True)
    base_code = models.URLField(blank=True)
    developer = models.ForeignKey(Developer, on_delete=models.CASCADE,
                                  related_name='projects')


class Portefolio(models.Model):
    name = models.CharField(max_length=255, blank=True)
    developer = models.OneToOneField(Developer, on_delete=models.CASCADE)
    projects = models.ManyToManyField(Project, blank=True)
    cover_image = models.ImageField(upload_to='portfolio_covers/', blank=True)
    slug = AutoSlugField(gettext_lazy("Slug"), populate_from=("name",))

    class Meta:
        verbose_name = "Portefolio"

    def __str__(self):
        """
        The string representation of this model is the slug.
        """
        return self.slug
