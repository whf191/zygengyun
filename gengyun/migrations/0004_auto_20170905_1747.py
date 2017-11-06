# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-05 17:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gengyun', '0003_zhongzi_create_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='gengyuns',
            name='update_date',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2017, 9, 5, 17, 47, 41, 864000)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='zhongzi',
            name='update_date',
            field=models.DateTimeField(auto_now=True, default=datetime.datetime(2017, 9, 5, 17, 47, 47, 759000)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='gengyuns',
            name='create_date',
            field=models.DateTimeField(auto_created=True),
        ),
        migrations.AlterField(
            model_name='zhongzi',
            name='create_date',
            field=models.DateTimeField(auto_created=True),
        ),
    ]