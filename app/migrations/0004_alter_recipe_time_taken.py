# Generated by Django 5.1.2 on 2024-10-18 01:05

import banjo.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_recipe_time_taken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='time_taken',
            field=banjo.models.IntegerField(default=0),
        ),
    ]
