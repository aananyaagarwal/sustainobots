# Generated by Django 5.1.3 on 2024-11-16 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("postgres_db_django_app", "0002_alter_publication_data"),
    ]

    operations = [
        migrations.AlterField(
            model_name="publication",
            name="url",
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
