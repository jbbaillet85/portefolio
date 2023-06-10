# Generated by Django 4.2.2 on 2023-06-09 13:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='projects', to='portefolio.developer')),
            ],
        ),
        migrations.CreateModel(
            name='Portefolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255)),
                ('cover_image', models.ImageField(blank=True, upload_to='portfolio_covers/')),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from=('name',), verbose_name='Slug')),
                ('developer', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='portefolio.developer')),
                ('projects', models.ManyToManyField(blank=True, to='portefolio.project')),
            ],
            options={
                'verbose_name': 'Portefolio',
            },
        ),
        migrations.AddField(
            model_name='developer',
            name='skills',
            field=models.ManyToManyField(blank=True, to='portefolio.skill'),
        ),
        migrations.AddField(
            model_name='developer',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]