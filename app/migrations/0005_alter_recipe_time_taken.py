# Generated by Django 5.1.2 on 2024-10-18 01:06

import banjo.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_recipe_time_taken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='time_taken',
            field=banjo.models.StringField(default=''),
        ),
    ]
