# Generated by Django 3.0.8 on 2020-07-24 08:20

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collections',
            name='movies',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.UUIDField(), default=list, size=None),
        ),
    ]
