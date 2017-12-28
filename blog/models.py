from __future__ import unicode_literals

from django.db import models


# Create your models here.
class TypechoComments(models.Model):
    coid = models.AutoField(primary_key=True)
    cid = models.IntegerField(blank=True, null=True)
    created = models.IntegerField(blank=True, null=True)
    author = models.CharField(max_length=200, blank=True, null=True)
    authorid = models.IntegerField(db_column='authorId', blank=True, null=True)  # Field name made lowercase.
    ownerid = models.IntegerField(db_column='ownerId', blank=True, null=True)  # Field name made lowercase.
    mail = models.CharField(max_length=200, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    ip = models.CharField(max_length=64, blank=True, null=True)
    agent = models.CharField(max_length=200, blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    type = models.CharField(max_length=16, blank=True, null=True)
    status = models.CharField(max_length=16, blank=True, null=True)
    parent = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'typecho_comments'


class TypechoContents(models.Model):
    cid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, blank=True, null=True)
    slug = models.CharField(unique=True, max_length=200, blank=True, null=True)
    created = models.IntegerField(blank=True, null=True)
    modified = models.IntegerField(blank=True, null=True)
    text = models.TextField(blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    authorid = models.IntegerField(db_column='authorId', blank=True, null=True)  # Field name made lowercase.
    template = models.CharField(max_length=32, blank=True, null=True)
    type = models.CharField(max_length=16, blank=True, null=True)
    status = models.CharField(max_length=16, blank=True, null=True)
    password = models.CharField(max_length=32, blank=True, null=True)
    commentsnum = models.IntegerField(db_column='commentsNum', blank=True, null=True)  # Field name made lowercase.
    allowcomment = models.CharField(db_column='allowComment', max_length=1, blank=True,
                                    null=True)  # Field name made lowercase.
    allowping = models.CharField(db_column='allowPing', max_length=1, blank=True,
                                 null=True)  # Field name made lowercase.
    allowfeed = models.CharField(db_column='allowFeed', max_length=1, blank=True,
                                 null=True)  # Field name made lowercase.
    parent = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'typecho_contents'


class TypechoFields(models.Model):
    cid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    type = models.CharField(max_length=8, blank=True, null=True)
    str_value = models.TextField(blank=True, null=True)
    int_value = models.IntegerField(blank=True, null=True)
    float_value = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'typecho_fields'
        unique_together = (('cid', 'name'),)


class TypechoMetas(models.Model):
    mid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    slug = models.CharField(max_length=200, blank=True, null=True)
    type = models.CharField(max_length=32)
    description = models.CharField(max_length=200, blank=True, null=True)
    count = models.IntegerField(blank=True, null=True)
    order = models.IntegerField(blank=True, null=True)
    parent = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'typecho_metas'


class TypechoOptions(models.Model):
    name = models.CharField(primary_key=True, max_length=32)
    user = models.IntegerField()
    value = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'typecho_options'
        unique_together = (('name', 'user'),)


class TypechoRelationships(models.Model):
    cid = models.IntegerField(primary_key=True)
    mid = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'typecho_relationships'
        unique_together = (('cid', 'mid'),)


class TypechoUsers(models.Model):
    uid = models.AutoField(primary_key=True)
    name = models.CharField(unique=True, max_length=32, blank=True, null=True)
    password = models.CharField(max_length=64, blank=True, null=True)
    mail = models.CharField(unique=True, max_length=200, blank=True, null=True)
    url = models.CharField(max_length=200, blank=True, null=True)
    screenname = models.CharField(db_column='screenName', max_length=32, blank=True,
                                  null=True)  # Field name made lowercase.
    created = models.IntegerField(blank=True, null=True)
    activated = models.IntegerField(blank=True, null=True)
    logged = models.IntegerField(blank=True, null=True)
    group = models.CharField(max_length=16, blank=True, null=True)
    authcode = models.CharField(db_column='authCode', max_length=64, blank=True,
                                null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'typecho_users'
