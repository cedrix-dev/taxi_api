# Generated by Django 3.1.4 on 2020-12-31 14:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('my_api', '0003_auto_20201231_1426'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='passager',
            name='message',
        ),
    ]
