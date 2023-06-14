from django.db import models
from django.utils.translation import gettext_lazy
from django_extensions.db.fields import AutoSlugField
from django.contrib.auth import get_user_model

User = get_user_model()


class Techno(models.Model):
    name = models.CharField(max_length=256, )
    slug = AutoSlugField(gettext_lazy("Slug"),
                         populate_from=("name",),
                         unique=True,)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Technologies'

    def __str__(self) -> str:
        return self.slug


class Project(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(blank=True)
    techno = models.ManyToManyField(Techno, blank=True)
    base_code = models.URLField(blank=True, unique=True)
    developer = models.ForeignKey(User, on_delete=models.CASCADE,
                                  related_name='project')
    slug = AutoSlugField(gettext_lazy("Slug"),
                         populate_from=("developer", "name",),
                         unique=True)

    class Meta:
        ordering = ['name']
        verbose_name_plural = 'Projects'

    def __str__(self):
        return self.slug
