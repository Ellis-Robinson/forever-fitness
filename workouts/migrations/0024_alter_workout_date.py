# Generated by Django 3.2.7 on 2022-01-27 22:39

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0023_alter_workout_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 1, 28, 22, 39, 37, 430361, tzinfo=utc)),
        ),
    ]
