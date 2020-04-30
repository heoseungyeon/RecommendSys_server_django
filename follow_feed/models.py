# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


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



class UserManager(BaseUserManager):
    def create_user(self, user_id, user_email, password=None):
        if not user_email:
            raise ValueError("Users must have an email address")

        user = self.model(
            user_id=user_id,
            user_email=self.normalize_email(user_email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, user_email, password=None):
        user = self.create_user(
            user_id=user_id,
            user_email=self.normalize_email(user_email),
            password=password

        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):

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
    age = models.CharField(max_length=45, blank=True, null=True)
    sex = models.CharField(max_length=45, blank=True, null=True)

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    object = UserManager()
    USERNAME_FIELD = 'user_email'
    REQUIRED_FIELDS = ['user_id']

    class Meta:
        db_table = 'user'



class UserLikeHistory(models.Model):
    idx = models.AutoField(primary_key=True)
    posting_idx = models.ForeignKey(UserPlaceHistory, models.DO_NOTHING, db_column='posting_idx', blank=True, null=True)
    user_idx = models.ForeignKey(User, models.DO_NOTHING, db_column='user_idx', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_like_history'
        unique_together = (('posting_idx', 'user_idx'),)


class UserFollow(models.Model):
    idx = models.AutoField(primary_key=True)
    user_idx = models.ForeignKey(User, models.DO_NOTHING, db_column='user_idx',related_name='follow_user')
    following_idx = models.ForeignKey(User, models.DO_NOTHING, db_column='following_idx',related_name='following_user')

    class Meta:
        managed = False
        db_table = 'user_follow'
        unique_together = (('user_idx', 'following_idx'),)


class PostingReviews(models.Model):
    idx = models.AutoField(primary_key=True)
    posting_idx = models.ForeignKey('UserPlaceHistory', models.DO_NOTHING, db_column='posting_idx', blank=True, null=True)
    user_idx = models.ForeignKey('User', models.DO_NOTHING, db_column='user_idx', blank=True, null=True)
    context = models.TextField(blank=True, null=True)
    date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'posting_reviews'
