# Generated by Django 5.0.6 on 2024-05-16 05:20

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("register", "0006_alter_user_hobby"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="hobby",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
