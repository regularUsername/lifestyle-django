# Generated by Django 4.0.2 on 2022-03-16 22:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rezepte', '0010_favorite_unique_favorite'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Favorite',
        ),
    ]