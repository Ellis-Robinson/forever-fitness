# Generated by Django 3.2.7 on 2022-01-20 16:18

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0015_auto_20220120_1615'),
    ]

    operations = [
        migrations.AddField(
            model_name='type_of_workout',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='workout',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 1, 21, 16, 18, 0, 176703, tzinfo=utc)),
        ),
    ]
