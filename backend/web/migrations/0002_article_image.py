# Generated by Django 4.1.3 on 2023-06-20 21:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="article",
            name="image",
            field=models.ImageField(null=True, upload_to=""),
        ),
    ]
