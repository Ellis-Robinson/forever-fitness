# Generated by Django 3.2.7 on 2022-01-14 08:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0001_initial'),
        ('workouts', '0005_auto_20220113_2159'),
    ]

    operations = [
        migrations.AddField(
            model_name='workout',
            name='users',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='profiles.userprofile'),
        ),
        migrations.DeleteModel(
            name='User_workouts',
        ),
    ]
