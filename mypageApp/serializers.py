from loginApp.models import *
from rest_framework import serializers

from .models import *


class UserPlaceHistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserPlaceHistory
        fields = '__all__'
        read_only_fields = ('idx',)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['idx', "nickname", 'image',"sex", 'age', 'description']


class UserLikeSerializer(serializers.ModelSerializer):

    posting = UserPlaceHistorySerializer(source='posting_idx')
    class Meta:
        model = UserLikeHistory
        fields = [ 'posting']
        read_only_fields = ('idx',)


class MyPageSerializer(serializers.ModelSerializer):
    like_history = UserLikeSerializer(source='mypage_userlikehistory_set', many=True)

    class Meta:
        model = User
        fields = ('idx', "nickname", 'user_nm', 'image', "sex", 'age', 'description', 'posting_cnt', 'following_cnt', 'follower_cnt', 'like_history')
        read_only_fields = ('idx',)


class UserPageSerializer(serializers.ModelSerializer):

    posting = UserPlaceHistorySerializer(source='userplacehistory_set', many=True)

    class Meta:
        model = User
        fields = ('idx', 'nickname', "sex", 'age', 'description', 'posting_cnt', 'following_cnt', 'follower_cnt', 'posting')
        read_only_fields = ('idx',)

