# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-09-07 10:42
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gengyun', '0004_auto_20170905_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='zhongzi',
            name='user_id',
            field=models.ForeignKey(default=1, help_text='\u7528\u6237\u7ed1\u5b9a', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='\u7528\u6237'),
            preserve_default=False,
        ),
    ]
