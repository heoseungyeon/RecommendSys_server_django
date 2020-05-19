from django.db import models
from loginApp.models import User
from recommendApp.models import *

# Create your models here.


class UserPick(models.Model):
    idx = models.AutoField(primary_key=True)
    user_idx = models.ForeignKey(User, models.DO_NOTHING, db_column='user_idx', blank=True, null=True, related_name = 'home_userpick_set')
    place_id = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_pick'
        unique_together = (('user_idx', 'place_id'),)

