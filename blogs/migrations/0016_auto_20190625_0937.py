# Generated by Django 2.2.2 on 2019-06-25 09:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0015_auto_20190625_0933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 25, 9, 37, 31, 922549)),
        ),
    ]