# Generated by Django 3.2.25 on 2024-03-08 09:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20240308_1032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2024, 3, 8, 10, 33, 47, 360072)),
        ),
    ]
