# Generated by Django 3.1.6 on 2021-05-21 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intentions', '0005_auto_20210521_1033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='public',
            field=models.BooleanField(default=False),
        ),
    ]
