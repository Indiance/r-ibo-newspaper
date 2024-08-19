# Generated by Django 4.2.2 on 2024-08-19 16:24

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):
    dependencies = [
        ("web", "0013_classification_slug_alter_article_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="article",
            name="article_id",
            field=models.UUIDField(default=uuid.uuid4, editable=False, unique=True),
        ),
    ]
