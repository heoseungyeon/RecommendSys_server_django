# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user_id = models.IntegerField(unique=True)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class CategoryImageM(models.Model):
    ctgr_mid = models.AutoField(primary_key=True)
    ctgr_name = models.CharField(max_length=45)
    large = models.ForeignKey('CategoryL', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_image_m'


class CategoryImageS(models.Model):
    ctgr_sid = models.AutoField(primary_key=True)
    ctgr_name = models.CharField(max_length=45, blank=True, null=True)
    large = models.ForeignKey(CategoryImageM, models.DO_NOTHING, blank=True, null=True)
    middle = models.ForeignKey(CategoryImageM, models.DO_NOTHING, blank=True, null=True)
    ctgr_name_en = models.CharField(max_length=45, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_image_s'
        unique_together = (('ctgr_name', 'middle'),)


class CategoryL(models.Model):
    ctgr_lid = models.AutoField(primary_key=True)
    ctgr_name = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'category_l'


class CategoryTextM(models.Model):
    ctgr_id = models.AutoField(primary_key=True)
    ctgr_name = models.CharField(max_length=45, blank=True, null=True)
    large = models.ForeignKey(CategoryL, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_text_m'


class CategoryTextS(models.Model):
    ctgr_id = models.AutoField(primary_key=True)
    ctgr_name = models.CharField(max_length=45, blank=True, null=True)
    middle = models.ForeignKey(CategoryTextM, models.DO_NOTHING, blank=True, null=True)
    large = models.ForeignKey(CategoryL, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'category_text_s'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class ImageMHistory(models.Model):
    idx = models.AutoField(primary_key=True)
    user_idx = models.ForeignKey('User', models.DO_NOTHING, db_column='user_idx')
    ctgr_idx = models.ForeignKey(CategoryImageM, models.DO_NOTHING, db_column='ctgr_idx')
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'image_m_history'


class ImageMScore(models.Model):
    idx = models.AutoField(primary_key=True)
    user_idx = models.ForeignKey('User', models.DO_NOTHING, db_column='user_idx', blank=True, null=True)
    image_ctgr_idx = models.ForeignKey(CategoryImageM, models.DO_NOTHING, db_column='image_ctgr_idx', blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    posting_idx = models.ForeignKey('UserPlaceHistory', models.DO_NOTHING, db_column='posting_idx', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'image_m_score'


class ImageSHistory(models.Model):
    idx = models.AutoField(primary_key=True)
    user_idx = models.ForeignKey('User', models.DO_NOTHING, db_column='user_idx')
    ctgr_idx = models.ForeignKey(CategoryImageS, models.DO_NOTHING, db_column='ctgr_idx')
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'image_s_history'


class ImageSScore(models.Model):
    idx = models.AutoField(primary_key=True)
    user_idx = models.ForeignKey('User', models.DO_NOTHING, db_column='user_idx', blank=True, null=True)
    image_ctgr_idx = models.ForeignKey(CategoryImageS, models.DO_NOTHING, db_column='image_ctgr_idx', blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    posting_idx = models.ForeignKey('UserPlaceHistory', models.DO_NOTHING, db_column='posting_idx', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'image_s_score'


class KnoxAuthtoken(models.Model):
    digest = models.CharField(primary_key=True, max_length=128)
    salt = models.CharField(unique=True, max_length=16)
    created = models.DateTimeField()
    user = models.ForeignKey('User', models.DO_NOTHING)
    expiry = models.DateTimeField(blank=True, null=True)
    token_key = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'knox_authtoken'


class PostingReviews(models.Model):
    idx = models.AutoField(primary_key=True)
    posting_idx = models.ForeignKey('UserPlaceHistory', models.DO_NOTHING, db_column='posting_idx', blank=True, null=True)
    user_idx = models.ForeignKey('User', models.DO_NOTHING, db_column='user_idx', blank=True, null=True)
    context = models.TextField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'posting_reviews'


class TextMHistory(models.Model):
    idx = models.AutoField(primary_key=True)
    user_idx = models.ForeignKey('User', models.DO_NOTHING, db_column='user_idx')
    ctgr_idx = models.ForeignKey(CategoryTextM, models.DO_NOTHING, db_column='ctgr_idx')
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'text_m_history'


class TextMScore(models.Model):
    idx = models.AutoField(primary_key=True)
    user_idx = models.ForeignKey('User', models.DO_NOTHING, db_column='user_idx', blank=True, null=True)
    text_ctgr_idx = models.ForeignKey(CategoryTextM, models.DO_NOTHING, db_column='text_ctgr_idx', blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    posting_idx = models.ForeignKey('UserPlaceHistory', models.DO_NOTHING, db_column='posting_idx', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'text_m_score'


class TextSHistory(models.Model):
    idx = models.AutoField(primary_key=True)
    user_idx = models.ForeignKey('User', models.DO_NOTHING, db_column='user_idx')
    ctgr_idx = models.ForeignKey(CategoryTextS, models.DO_NOTHING, db_column='ctgr_idx')
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'text_s_history'


class TextSScore(models.Model):
    idx = models.AutoField(primary_key=True)
    user_idx = models.ForeignKey('User', models.DO_NOTHING, db_column='user_idx', blank=True, null=True)
    text_ctgr_idx = models.ForeignKey(CategoryTextS, models.DO_NOTHING, db_column='text_ctgr_idx', blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    posting_idx = models.ForeignKey('UserPlaceHistory', models.DO_NOTHING, db_column='posting_idx', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'text_s_score'


class User(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    idx = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=100, blank=True, null=True)
    user_nm = models.CharField(max_length=50, blank=True, null=True)
    user_email = models.CharField(unique=True, max_length=100, blank=True, null=True)
    posting_cnt = models.IntegerField(blank=True, null=True)
    following_cnt = models.IntegerField(blank=True, null=True)
    follower_cnt = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    age = models.DateField(blank=True, null=True)
    sex = models.CharField(max_length=45, blank=True, null=True)
    is_admin = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'user'


class UserFollow(models.Model):
    idx = models.AutoField(primary_key=True)
    user_idx = models.ForeignKey(User, models.DO_NOTHING, db_column='user_idx')
    following_idx = models.ForeignKey(User, models.DO_NOTHING, db_column='following_idx')

    class Meta:
        managed = False
        db_table = 'user_follow'
        unique_together = (('user_idx', 'following_idx'),)


class UserLHistory(models.Model):
    idx = models.AutoField(primary_key=True)
    user_idx = models.ForeignKey(User, models.DO_NOTHING, db_column='user_idx')
    ctgr_idx = models.ForeignKey(CategoryL, models.DO_NOTHING, db_column='ctgr_idx')
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_l_history'
        unique_together = (('user_idx', 'ctgr_idx'),)


class UserLScore(models.Model):
    idx = models.AutoField(primary_key=True)
    user_idx = models.ForeignKey(User, models.DO_NOTHING, db_column='user_idx', blank=True, null=True)
    ctgr_idx = models.ForeignKey(CategoryL, models.DO_NOTHING, db_column='ctgr_idx', blank=True, null=True)
    score = models.FloatField(blank=True, null=True)
    posting_idx = models.ForeignKey('UserPlaceHistory', models.DO_NOTHING, db_column='posting_idx', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_l_score'


class UserLikeHistory(models.Model):
    idx = models.AutoField(primary_key=True)
    posting_idx = models.ForeignKey('UserPlaceHistory', models.DO_NOTHING, db_column='posting_idx', blank=True, null=True)
    user_idx = models.ForeignKey(User, models.DO_NOTHING, db_column='user_idx', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_like_history'
        unique_together = (('posting_idx', 'user_idx'),)


class UserPick(models.Model):
    idx = models.AutoField(primary_key=True)
    user_idx = models.ForeignKey(User, models.DO_NOTHING, db_column='user_idx', blank=True, null=True)
    place_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_pick'
        unique_together = (('user_idx', 'place_id'),)


class UserPlaceHistory(models.Model):
    idx = models.AutoField(primary_key=True)
    user_idx = models.ForeignKey(User, models.DO_NOTHING, db_column='user_idx', blank=True, null=True)
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


class VoiceRecognitionPost(models.Model):
    title = models.CharField(max_length=144)
    subtitle = models.CharField(max_length=144, blank=True, null=True)
    content = models.TextField()
    created_at = models.DateTimeField()
    user_id = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'voice_recognition_post'
