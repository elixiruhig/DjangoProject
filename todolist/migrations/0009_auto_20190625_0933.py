# Generated by Django 2.2.2 on 2019-06-25 09:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0008_auto_20190625_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='created',
            field=models.DateField(default=datetime.datetime(2019, 6, 25, 9, 33, 44, 854253, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='duedate',
            field=models.DateField(default=datetime.datetime(2019, 6, 25, 9, 33, 44, 854279, tzinfo=utc)),
        ),
    ]