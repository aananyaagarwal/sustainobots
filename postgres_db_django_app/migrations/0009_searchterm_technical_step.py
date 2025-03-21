# Generated by Django 5.1.3 on 2024-11-17 00:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("postgres_db_django_app", "0008_metric_crop"),
    ]

    operations = [
        migrations.AddField(
            model_name="searchterm",
            name="technical_step",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="search_terms",
                to="postgres_db_django_app.technicalstep",
            ),
        ),
    ]
