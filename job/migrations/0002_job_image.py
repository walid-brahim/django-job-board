# Generated by Django 3.0.8 on 2020-07-17 20:31

from django.db import migrations, models
import job.models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='image',
            field=models.ImageField(default='', upload_to=job.models.uploadimage),
            preserve_default=False,
        ),
    ]
