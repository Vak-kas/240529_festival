# Generated by Django 5.0.5 on 2024-05-09 16:56

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="User",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("nickname", models.CharField(max_length=20, unique=True)),
                ("age", models.IntegerField()),
                ("instagram_id", models.CharField(max_length=50, unique=True)),
                ("hobby", models.CharField(max_length=50)),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "Male"), ("F", "Female")], max_length=1
                    ),
                ),
            ],
        ),
    ]
