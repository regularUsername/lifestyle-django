# Generated by Django 4.0.2 on 2022-02-21 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rezepte', '0005_rezept_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='rezept',
            name='text',
        ),
        migrations.AlterField(
            model_name='rezept',
            name='thumbnail',
            field=models.ImageField(blank=True, upload_to='uploads/'),
        ),
    ]
