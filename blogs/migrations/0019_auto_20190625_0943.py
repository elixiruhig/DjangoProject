# Generated by Django 2.2.2 on 2019-06-25 09:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0018_auto_20190625_0941'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 25, 9, 43, 34, 550025)),
        ),
    ]
