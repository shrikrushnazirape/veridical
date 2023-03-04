# Generated by Django 4.1.7 on 2023-03-04 10:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Prediction",
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
                ("storage", models.IntegerField(default=0)),
                ("security", models.IntegerField(default=0)),
                ("access", models.IntegerField(default=0)),
                ("support", models.IntegerField(default=0)),
                ("computation", models.IntegerField(default=0)),
                ("vulnerability", models.IntegerField(default=0)),
                ("apiCalls", models.IntegerField(default=0)),
                ("apiCustumize", models.IntegerField(default=0)),
                ("computationIns", models.IntegerField(default=0)),
                ("serverLoc", models.IntegerField(default=0)),
            ],
        ),
    ]
