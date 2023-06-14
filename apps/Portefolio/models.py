from django.db import models
from django.utils.translation import gettext_lazy
from django_extensions.db.fields import AutoSlugField
from django.contrib.auth import get_user_model
from apps.project.models import Project


class Portefolio(models.Model):
    name = models.CharField(max_length=255, blank=True)
    developer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    projects = models.ManyToManyField(Project, blank=True)
    cover_image = models.ImageField(upload_to='portfolio_covers/', blank=True)
    slug = AutoSlugField(gettext_lazy("Slug"),
                         populate_from=("developer",
                                        "name",),
                         unique=True)

    class Meta:
        verbose_name = "Portefolio"

    def __str__(self):
        """
        The string representation of this model is the slug.
        """
        return self.slug
