# Generated by Django 4.2.17 on 2025-02-11 14:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0019_alter_comment_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2025, 2, 11, 14, 43, 43, 529809, tzinfo=datetime.timezone.utc)),
        ),
    ]
