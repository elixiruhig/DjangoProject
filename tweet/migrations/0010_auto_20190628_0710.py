# Generated by Django 2.2.2 on 2019-06-28 07:10

import datetime
from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('tweet', '0009_auto_20190628_0703'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='hashtags',
        ),
        migrations.AddField(
            model_name='tweet',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='tweet',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 28, 7, 10, 46, 245100)),
        ),
    ]
