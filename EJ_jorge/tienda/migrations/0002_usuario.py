# Generated by Django 4.2.6 on 2023-11-10 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=254)),
                ('correo', models.EmailField(max_length=254)),
                ('clave', models.CharField(max_length=254)),
                ('rol', models.IntegerField(choices=[(1, 'Administrador'), (2, 'Despachador'), (3, 'Cliente')], default=3)),
                ('foto', models.ImageField(upload_to='tienda/')),
            ],
        ),
    ]
