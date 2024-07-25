# Generated by Django 4.1.13 on 2024-06-14 06:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("database", "0158_field_description"),
        ("baserow_enterprise", "0025_authformelement"),
    ]

    operations = [
        migrations.AddField(
            model_name="localbaserowusersource",
            name="role_field",
            field=models.ForeignKey(
                help_text="The Baserow field that contains the role of the user.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="+",
                to="database.field",
            ),
        ),
    ]