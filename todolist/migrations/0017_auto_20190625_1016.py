# Generated by Django 2.2.2 on 2019-06-25 10:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0016_auto_20190625_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='created',
            field=models.DateField(default=datetime.datetime(2019, 6, 25, 10, 16, 37, 268853, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='duedate',
            field=models.DateField(default=datetime.datetime(2019, 6, 25, 10, 16, 37, 268879, tzinfo=utc)),
        ),
    ]