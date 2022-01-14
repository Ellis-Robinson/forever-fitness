# Generated by Django 3.2.7 on 2022-01-13 20:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('workouts', '0003_auto_20220113_1951'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_workouts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('workout', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workouts', to='workouts.workout')),
            ],
            options={
                'verbose_name_plural': 'User Workouts',
            },
        ),
    ]