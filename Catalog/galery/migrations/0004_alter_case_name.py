# Generated by Django 5.0.4 on 2024-04-10 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galery', '0003_delete_album_delete_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='case',
            name='name',
            field=models.CharField(max_length=250, verbose_name='Автор'),
        ),
    ]
