# Generated by Django 4.1.1 on 2023-03-04 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("Predict", "0002_prediction_ans"),
    ]

    operations = [
        migrations.RemoveField(model_name="prediction", name="ans",),
    ]
