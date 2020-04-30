from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.

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

