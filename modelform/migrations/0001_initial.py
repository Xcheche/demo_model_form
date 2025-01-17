# Generated by Django 5.0.6 on 2024-08-07 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                (
                    "name",
                    models.CharField(
                        help_text="Enter project name",
                        max_length=100,
                        verbose_name="Project Name",
                    ),
                ),
                (
                    "assigned_to",
                    models.CharField(max_length=100, verbose_name="Assigned To"),
                ),
                ("priority", models.IntegerField()),
            ],
        ),
    ]
