# Generated by Django 2.2.2 on 2019-06-27 06:03

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('todolist', '0020_auto_20190626_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='created',
            field=models.DateField(default=datetime.datetime(2019, 6, 27, 6, 3, 39, 735191, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='todolist',
            name='duedate',
            field=models.DateField(default=datetime.datetime(2019, 6, 27, 6, 3, 39, 735230, tzinfo=utc)),
        ),
    ]
