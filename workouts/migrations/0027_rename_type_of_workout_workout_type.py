# Generated by Django 3.2.7 on 2022-02-10 18:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0026_auto_20220210_1715'),
    ]

    operations = [
        migrations.RenameField(
            model_name='workout',
            old_name='type_of_workout',
            new_name='type',
        ),
    ]