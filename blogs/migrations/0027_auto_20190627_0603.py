# Generated by Django 2.2.2 on 2019-06-27 06:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0026_auto_20190626_0917'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 27, 6, 3, 39, 732657)),
        ),
    ]
