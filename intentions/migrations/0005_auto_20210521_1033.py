# Generated by Django 3.1.6 on 2021-05-21 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intentions', '0004_auto_20210521_1026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='public',
            field=models.BooleanField(),
        ),
    ]
