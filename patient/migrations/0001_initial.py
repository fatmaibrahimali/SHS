# Generated by Django 4.0.2 on 2022-02-15 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='UserVital',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heart_rate', models.IntegerField(default=0)),
                ('blood_pressure_up', models.IntegerField(default=0)),
                ('blood_pressure_down', models.IntegerField(default=0)),
                ('respiration_rate', models.IntegerField(default=0)),
                ('temprature', models.DecimalField(decimal_places=1, default=0, max_digits=3)),
            ],
        ),
    ]