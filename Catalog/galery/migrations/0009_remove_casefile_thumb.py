# Generated by Django 5.0.4 on 2024-04-17 03:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('galery', '0008_casefile_thumb'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='casefile',
            name='thumb',
        ),
    ]
