# Generated by Django 2.2.8 on 2020-03-29 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Repuesto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Descripcion', models.CharField(max_length=200)),
                ('Foto', models.ImageField(upload_to='PocketGarage/repuestos/')),
                ('Precio', models.CharField(max_length=25)),
                ('CI', models.IntegerField(default=0)),
                ('Nombre_Vendedor', models.CharField(max_length=150)),
                ('Telefono_Vendedor', models.IntegerField()),
                ('Email_Vendedor', models.EmailField(blank=True, max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CI', models.IntegerField(unique=True)),
                ('Nombre', models.CharField(max_length=50)),
                ('Telefono', models.IntegerField()),
                ('Email', models.EmailField(blank=True, max_length=254)),
                ('Contraseña', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Marca', models.CharField(max_length=25)),
                ('Modelo', models.CharField(max_length=25)),
                ('Año', models.IntegerField()),
                ('Color', models.CharField(max_length=30)),
                ('Motor', models.CharField(max_length=20)),
                ('Precio', models.CharField(max_length=25)),
                ('Foto', models.ImageField(upload_to='PocketGarage/vehiculos/')),
                ('Especificaciones', models.CharField(max_length=500)),
                ('CI', models.IntegerField(default=0)),
                ('Nombre_Propietario', models.CharField(max_length=150)),
                ('Telefono_Propietario', models.IntegerField()),
                ('Email_Propietario', models.EmailField(blank=True, max_length=254)),
            ],
        ),
    ]
