# Generated by Django 5.0.6 on 2024-05-14 05:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("find", "0002_visitor_age"),
    ]

    operations = [
        migrations.AlterField(
            model_name="visitor",
            name="keyword",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
