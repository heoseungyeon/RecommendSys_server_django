from loginApp.models import *
from rest_framework import serializers
from recommendApp.models import UserPlaceHistory


class MyPageSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("user_id", "sex", 'age', 'description', 'posting_cnt', 'following_cnt', 'follower_cnt')


class UserPlaceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPlaceHistory
        fields = ('idx','place_id')


class UserPageSerializer(serializers.ModelSerializer):

    posting = UserPlaceHistorySerializer(source='userplacehistory_set', many=True)

    class Meta:
        model = User
        fields = ('idx', 'user_id', "sex", 'age', 'description', 'posting_cnt', 'following_cnt', 'follower_cnt', 'posting')


