# Generated by Django 4.0.2 on 2024-06-01 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0004_keywordsearch_last_api_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='keywordsearch',
            name='search_count',
            field=models.IntegerField(default=0),
        ),
    ]
