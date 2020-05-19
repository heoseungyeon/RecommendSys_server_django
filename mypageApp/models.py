from django.db import models
from loginApp.models import User
from recommendApp.models import UserPlaceHistory
# Create your models here.
class UserLikeHistory(models.Model):
    idx = models.AutoField(primary_key=True)
    posting_idx = models.ForeignKey(UserPlaceHistory, models.DO_NOTHING, db_column='posting_idx', blank=True, null=True)
    user_idx = models.ForeignKey(User, models.DO_NOTHING, db_column='user_idx', blank=True, null=True, related_name = 'mypage_userlikehistory_set')

    class Meta:
        managed = False
        db_table = 'user_like_history'
        unique_together = (('posting_idx', 'user_idx'),)