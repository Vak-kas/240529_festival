# Generated by Django 5.0.6 on 2024-05-14 05:33

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("register", "0004_delete_backup_user_is_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="hobby",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
