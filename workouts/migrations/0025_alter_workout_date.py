# Generated by Django 3.2.7 on 2022-01-28 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0024_alter_workout_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workout',
            name='date',
            field=models.DateTimeField(),
        ),
    ]