# Generated by Django 2.2.2 on 2019-06-27 10:07

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0024_auto_20190627_0853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='created',
            field=models.DateField(default=datetime.datetime(2019, 6, 27, 10, 7, 33, 908752, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='duedate',
            field=models.DateField(default=datetime.datetime(2019, 6, 27, 10, 7, 33, 908779, tzinfo=utc)),
        ),
    ]
