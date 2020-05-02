from rest_framework import serializers
from .models import *


class PostingReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostingReviews
        fields = '__all__'

class CommentsSerializer(serializers.ModelSerializer):

    comment = PostingReviewSerializer(source='postingreviews_set', many=True)

    class Meta:
        model = UserPlaceHistory
        fields = ('idx', 'date', 'context', 'comment')
