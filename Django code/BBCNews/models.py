from __future__ import unicode_literals

from django.db import models


class bbcnews(models.Model):
    title = models.CharField(db_column='title',max_length=100, blank=True, null=False)
    url = models.CharField(db_column='url',max_length=100, blank=True, null=False)
    content = models.TextField(db_column='content',blank=True, null=True)
    
    class Meta:
        managed = False
        db_table = 'bbcnews'
