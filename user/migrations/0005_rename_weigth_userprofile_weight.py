# Generated by Django 4.0.2 on 2022-02-14 01:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_rename_heigth_userprofile_height'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='weigth',
            new_name='weight',
        ),
    ]
