# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Bkuser(models.Model):
    username = models.CharField(max_length=32,
                                verbose_name='User Name')
    useremail = models.EmailField(max_length=128,
                                  verbose_name='User Email')
    password = models.CharField(max_length=64,
                                verbose_name='Password')
    registered_dttm = models.DateTimeField(auto_now_add=True,
                                           verbose_name='Time created')

    def __str__(self):
        return self.username

    class Meta:
        db_table = 'brandon_user'
        # App Name change
        verbose_name_plural = "Brandon's Users"