# Generated by Django 3.2.5 on 2024-10-31 16:10

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0014_auto_20241031_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 10, 31, 16, 10, 39, 660229, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='curio',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='news.curio'),
        ),
    ]
