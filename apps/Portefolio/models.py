from django.db import models
from django_extensions.db.fields import AutoSlugField

# Create your models here.
class Portefolio(models.Model):
    name = models.CharField(
        max_length=255, unique=True,
        verbose_name="Portefolio", default=""
    )
    slug = AutoSlugField(gettext_lazy("Slug"), populate_from=("name",))

    class Meta:
        verbose_name = "Portefolio"

    def __str__(self):
        """
        The string representation of this model is the slug.
        """
        return self.slug