# Generated by Django 5.1 on 2024-09-05 02:22

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0015_issue_article_issue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='issue',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='issueWhenPublished', to='web.issue'),
        ),
    ]
