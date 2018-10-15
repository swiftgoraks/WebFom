# Generated by Django 2.1.2 on 2018-10-15 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0006_auto_20181014_1734'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('carnet', models.CharField(max_length=10)),
                ('sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], default='M', max_length=1)),
            ],
        ),
        migrations.RemoveField(
            model_name='ingresarproduct',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Username',
        ),
        migrations.DeleteModel(
            name='IngresarProduct',
        ),
    ]