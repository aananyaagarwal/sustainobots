# Generated by Django 5.1.3 on 2024-11-17 01:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("postgres_db_django_app", "0009_searchterm_technical_step"),
    ]

    operations = [
        migrations.AddField(
            model_name="metric",
            name="notes",
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="metric",
            name="publication",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="metrics",
                to="postgres_db_django_app.publication",
            ),
        ),
        migrations.AddField(
            model_name="metric",
            name="units",
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name="metric",
            name="value",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
