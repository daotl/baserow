# Generated by Django 4.1.13 on 2024-04-26 21:11

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("builder", "0015_refreshdatasourceworkflowaction"),
    ]

    operations = [
        migrations.AlterField(
            model_name="element",
            name="visibility",
            field=models.CharField(
                choices=[
                    ("all", "All"),
                    ("logged-in", "Logged In"),
                    ("not-logged", "Not Logged"),
                ],
                db_index=True,
                default="all",
                max_length=20,
            ),
        ),
    ]