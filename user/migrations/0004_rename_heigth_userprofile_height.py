# Generated by Django 4.0.2 on 2022-02-14 00:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_uservital_userprofile'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='heigth',
            new_name='height',
        ),
    ]