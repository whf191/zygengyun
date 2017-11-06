#coding=utf-8
from __future__ import unicode_literals

from django.db import models
from  django.contrib.auth.models import User

# Create your models here.


class   gengyuns(models.Model):
    user_id = models.ForeignKey(User,verbose_name="用户",help_text="用户绑定")
    name =  models.CharField(max_length=255,verbose_name="耕耘",help_text="开垦荒地")
    text = models.TextField(verbose_name="荒地描述",blank=True)
    create_date = models.DateTimeField(auto_created=True)
    update_date = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return "{0}({1})".format(self.user_id,self.name)


class zhongzi(models.Model):
    gengyuns_id = models.ForeignKey(gengyuns,verbose_name="耕耘",help_text="绑定荒地")
    user_id = models.ForeignKey(User, verbose_name="用户", help_text="用户绑定")
    name = models.CharField(max_length=255,verbose_name="播种")
    text = models.TextField(verbose_name="种子描述")
    create_date = models.DateTimeField(auto_created=True)
    update_date = models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return "{0}({0})".format(self.gengyuns_id,self.name)
