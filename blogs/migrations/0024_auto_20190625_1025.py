# Generated by Django 2.2.2 on 2019-06-25 10:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0023_auto_20190625_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 25, 10, 25, 10, 774963)),
        ),
    ]
