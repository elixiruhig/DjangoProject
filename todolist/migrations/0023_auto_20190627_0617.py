# Generated by Django 2.2.2 on 2019-06-27 06:17

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0022_auto_20190627_0606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='created',
            field=models.DateField(default=datetime.datetime(2019, 6, 27, 6, 17, 50, 128951, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='duedate',
            field=models.DateField(default=datetime.datetime(2019, 6, 27, 6, 17, 50, 128976, tzinfo=utc)),
        ),
    ]
