# Generated by Django 2.1.2 on 2018-10-14 20:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Usuario',
            new_name='Username',
        ),
        migrations.RenameField(
            model_name='username',
            old_name='nom_usua',
            new_name='user',
        ),
    ]
