# Generated by Django 3.0.7 on 2020-06-04 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sound', '0002_soundpost_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='soundpost',
            name='title',
            field=models.CharField(default='sound file', max_length=100),
        ),
    ]