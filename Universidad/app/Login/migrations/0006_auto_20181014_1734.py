# Generated by Django 2.1.2 on 2018-10-14 23:34

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Login', '0005_ingresarproducto'),
    ]

    operations = [
        migrations.CreateModel(
            name='IngresarProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('producto', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=50)),
                ('precio', models.CharField(max_length=10)),
                ('usuario', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='IngresarProducto',
        ),
    ]