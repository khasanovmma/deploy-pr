# Generated by Django 4.0.4 on 2022-05-16 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_site', '0003_alter_profile_facebook_url_alter_profile_github_url_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.CharField(blank=True, max_length=155),
        ),
        migrations.AddField(
            model_name='profile',
            name='mobile',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='phone',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
