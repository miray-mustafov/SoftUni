# Generated by Django 4.1.2 on 2022-11-13 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_alter_album_options_profile_n'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='s',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
