# Generated by Django 4.2 on 2024-03-09 04:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_curio_event_delete_news'),
    ]

    operations = [
        migrations.RenameField(
            model_name='event',
            old_name='content',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='event',
            old_name='fecha_event',
            new_name='end_time',
        ),
        migrations.AddField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(null=True, verbose_name='Fecha del evento'),
        ),
    ]
