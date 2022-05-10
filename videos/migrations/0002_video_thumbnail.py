# Generated by Django 4.0.2 on 2022-04-16 19:31

from django.db import migrations, models
import videos.models


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='thumbnail',
            field=models.ImageField(default=None, upload_to=videos.models.video_thumbnail_path),
            preserve_default=False,
        ),
    ]
