from django.db import models
from django.contrib.auth.models import AbstractUser
from django_extensions.db.fields import AutoSlugField
from django.utils.translation import gettext_lazy


class Skill(models.Model):
    name = models.CharField(max_length=100)
    slug = AutoSlugField(gettext_lazy("Slug"),
                         populate_from=("name",),
                         unique=True,)

    def __str__(self) -> str:
        return self.slug


class User(AbstractUser):
    """Utilisateur personnalisé pour l'application."""
    bio = models.TextField(verbose_name='Biography',
                           help_text='Enter your bio here.', blank=True)
    skills = models.ManyToManyField('Skill', blank=True,
                                    verbose_name='Skills',
                                    help_text='''Select the skills that
                                    apply to this user''')

    def user_profile_upload_to(instance, filename):
        """Returns the upload path for user profile images."""
        return f'user_profile/{instance.email}/{filename}'

    image_profile = models.ImageField(upload_to=user_profile_upload_to,
                                      blank=True)

    slug = AutoSlugField(gettext_lazy("Slug"),
                         populate_from=("email"),
                         unique=True,)

    def __str__(self):
        return self.email
