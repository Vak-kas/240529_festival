# Generated by Django 5.0.6 on 2024-05-13 18:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("find", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="visitor",
            name="age",
            field=models.IntegerField(default=24),
            preserve_default=False,
        ),
    ]
