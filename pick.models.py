# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class User(models.Model):
    idx = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=100, blank=True, null=True)
    user_pw = models.CharField(max_length=150, blank=True, null=True)
    user_nm = models.CharField(max_length=50, blank=True, null=True)
    user_email = models.CharField(max_length=100, blank=True, null=True)
    posting_cnt = models.IntegerField(blank=True, null=True)
    following_cnt = models.IntegerField(blank=True, null=True)
    follower_cnt = models.IntegerField(blank=True, null=True)
    decription = models.TextField(blank=True, null=True)
    age = models.CharField(max_length=45, blank=True, null=True)
    sex = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
        unique_together = (('user_id', 'user_email'),)
# Unable to inspect table 'userpick'
# The error was: (1146, "Table 'recommendsys.userpick' doesn't exist")
