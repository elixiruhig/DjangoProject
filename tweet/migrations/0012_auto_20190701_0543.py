# Generated by Django 2.2.2 on 2019-07-01 05:43

import datetime
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tweet', '0011_auto_20190628_0718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 7, 1, 5, 43, 40, 886388)),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(default='profile_pic/default', upload_to='profile_pic'),
        ),
        migrations.CreateModel(
            name='Friend',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('users', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
