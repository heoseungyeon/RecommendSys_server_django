# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class UserFollow(models.Model):
    idx = models.AutoField(primary_key=True)
    user_idx = models.ForeignKey('User', models.DO_NOTHING,related_name='user_idx', db_column='user_idx')
    following_idx = models.ForeignKey('User', models.DO_NOTHING,related_name='following_idx', db_column='following_idx')

    class Meta:
        managed = False
        db_table = 'user_follow'
        unique_together = (('user_idx', 'following_idx'),)


class UserPlaceHistory(models.Model):
    idx = models.AutoField(primary_key=True)
    user_idx = models.ForeignKey('User', models.DO_NOTHING, db_column='user_idx', blank=True, null=True)
    place_id = models.CharField(max_length=100, blank=True, null=True)
    context = models.TextField(blank=True, null=True)
    img_cnt = models.IntegerField(blank=True, null=True)
    like_cnt = models.IntegerField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    tag_1 = models.CharField(max_length=45, blank=True, null=True)
    tag_2 = models.CharField(max_length=45, blank=True, null=True)
    tag_3 = models.CharField(max_length=45, blank=True, null=True)
    tag_4 = models.CharField(max_length=45, blank=True, null=True)
    tag_5 = models.CharField(max_length=45, blank=True, null=True)
    tag_6 = models.CharField(max_length=45, blank=True, null=True)
    rating = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_place_history'


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


class UserLScore(models.Model):
    idx = models.AutoField(primary_key=True)
    user_idx = models.ForeignKey(User, models.DO_NOTHING, db_column='user_idx', blank=True, null=True)
    ctgr_idx = models.ForeignKey('CategoryL', models.DO_NOTHING, db_column='ctgr_idx', blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    posting_idx = models.ForeignKey(UserPlaceHistory, models.DO_NOTHING, db_column='posting_idx', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_l_score'



class TextMScore(models.Model):
    idx = models.AutoField(primary_key=True)
    user_idx = models.ForeignKey(User, models.DO_NOTHING, db_column='user_idx', blank=True, null=True)
    text_ctgr_idx = models.ForeignKey('CategoryTextM', models.DO_NOTHING, db_column='text_ctgr_idx', blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    posting_idx = models.ForeignKey(UserPlaceHistory, models.DO_NOTHING, db_column='posting_idx', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'text_m_score'


class TextSScore(models.Model):
    idx = models.AutoField(primary_key=True)
    user_idx = models.ForeignKey(User, models.DO_NOTHING, db_column='user_idx', blank=True, null=True)
    text_ctgr_idx = models.ForeignKey('CategoryTextS', models.DO_NOTHING, db_column='text_ctgr_idx', blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    posting_idx = models.ForeignKey(UserPlaceHistory, models.DO_NOTHING, db_column='posting_idx', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'text_s_score'


class ImageMScore(models.Model):
    idx = models.AutoField(primary_key=True)
    user_idx = models.ForeignKey(User, models.DO_NOTHING, db_column='user_idx', blank=True, null=True)
    image_ctgr_idx = models.ForeignKey('CategoryImageM', models.DO_NOTHING, db_column='image_ctgr_idx', blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    posting_idx = models.ForeignKey(UserPlaceHistory, models.DO_NOTHING, db_column='posting_idx', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'image_m_score'


class ImageSScore(models.Model):
    idx = models.AutoField(primary_key=True)
    user_idx = models.IntegerField(blank=True, null=True)
    image_ctgr_idx = models.ForeignKey('CategoryImageS', models.DO_NOTHING, db_column='image_ctgr_idx', blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    posting_idx = models.ForeignKey(UserPlaceHistory, models.DO_NOTHING, db_column='posting_idx', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'image_s_score'


class CategoryL(models.Model):
    ctgr_lid = models.AutoField(primary_key=True)
    ctgr_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'category_l'


class CategoryTextM(models.Model):
    ctgr_id = models.AutoField(primary_key=True)
    ctgr_name = models.CharField(max_length=45, blank=True, null=True)
    large_id = models.ForeignKey(CategoryL, models.DO_NOTHING,db_column='large_id',related_name='large_id_textM', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_text_m'


class CategoryTextS(models.Model):
    ctgr_id = models.AutoField(primary_key=True)
    ctgr_name = models.CharField(max_length=45, blank=True, null=True)
    middle_id = models.ForeignKey(CategoryTextM, models.DO_NOTHING,db_column='middle_id',related_name='middle_id_textM', blank=True, null=True)
    large_id = models.ForeignKey(CategoryL, models.DO_NOTHING,db_column='large_id',related_name='large_id_textS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_text_s'


class CategoryImageM(models.Model):
    ctgr_mid = models.AutoField(primary_key=True)
    ctgr_name = models.CharField(max_length=45)
    large_id = models.ForeignKey(CategoryL, models.DO_NOTHING,db_column='large_id',related_name='large_id_imageM', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_image_m'


class CategoryImageS(models.Model):
    ctgr_sid = models.AutoField(primary_key=True)
    ctgr_name = models.CharField(max_length=45)
    large_id = models.ForeignKey(CategoryImageM, models.DO_NOTHING,db_column='large_id',related_name='large_id_imageS', blank=True, null=True)
    middle_id = models.ForeignKey(CategoryImageM, models.DO_NOTHING,db_column='middle_id',related_name='middle_id_imageS', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_image_s'
        unique_together = (('ctgr_name', 'middle_id'),)
