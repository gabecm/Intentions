# Generated by Django 3.1.6 on 2021-05-19 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('intentions', '0002_auto_20210519_0915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entry',
            name='headspace',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='entry',
            name='prompt_response',
            field=models.CharField(max_length=2000),
        ),
    ]
