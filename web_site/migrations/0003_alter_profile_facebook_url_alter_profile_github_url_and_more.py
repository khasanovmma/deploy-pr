# Generated by Django 4.0.4 on 2022-05-16 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_site', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='facebook_url',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='github_url',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='instagram_url',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='telegram_url',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='website_url',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
