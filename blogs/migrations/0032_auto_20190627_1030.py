# Generated by Django 2.2.2 on 2019-06-27 10:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0031_auto_20190627_1007'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 27, 10, 30, 27, 815568)),
        ),
    ]