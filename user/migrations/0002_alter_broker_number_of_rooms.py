# Generated by Django 5.0.4 on 2024-06-23 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='broker',
            name='number_of_rooms',
            field=models.PositiveBigIntegerField(),
        ),
    ]
