# Generated by Django 2.2.2 on 2019-06-18 08:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0009_auto_20190618_0830'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 18, 8, 33, 23, 750207)),
        ),
    ]
