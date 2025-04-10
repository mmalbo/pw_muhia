# Generated by Django 4.2.17 on 2025-01-26 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galeria', '0006_banner_pcpal'),
    ]

    operations = [
        migrations.CreateModel(
            name='carrusel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Nombre')),
                ('image', models.ImageField(upload_to='galeria', verbose_name='Imagen')),
                ('activo', models.BooleanField(default=True)),
                ('created', models.DateTimeField(auto_now=True, verbose_name='Fecha de creación')),
            ],
            options={
                'verbose_name': 'Catalogo',
                'verbose_name_plural': 'Catalogos',
                'db_table': 'carrusel',
                'ordering': ['created'],
            },
        ),
    ]
