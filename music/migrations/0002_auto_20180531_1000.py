# Generated by Django 2.0.5 on 2018-05-31 10:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='logo',
            new_name='album_logo',
        ),
        migrations.RenameField(
            model_name='album',
            old_name='title',
            new_name='album_title',
        ),
        migrations.RenameField(
            model_name='song',
            old_name='title',
            new_name='song_title',
        ),
    ]