# Generated by Django 5.0.6 on 2024-05-29 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0008_alter_user_instagram_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=20),
        ),
    ]
