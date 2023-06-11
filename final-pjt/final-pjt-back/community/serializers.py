from rest_framework import serializers
from .models import Review, Comment


class CommentSerializer(serializers.ModelSerializer):
    
    username = serializers.CharField(source='user.username', read_only=True)
    userImg = serializers.CharField(source='user.userImg',read_only=True)
    userpoint = serializers.IntegerField(source='user.point', read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'content','created_at','updated_at','review','user','username','userImg','userpoint')
        read_only_fields = ('review', 'user')

class ReviewSerializer(serializers.ModelSerializer):
    
    dislike_review_users_count = serializers.IntegerField(source='dislike_review_users.count', read_only=True)
    like_review_users_count = serializers.IntegerField(source='like_review_users.count', read_only=True)
    comment_set = CommentSerializer(many=True, read_only=True) # CommentSerializer정의가 이 코드보다 밑에 있다면 에러가 발생할 수 있음. json 안에 json 이 있는 형태가 됨
    comment_count = serializers.IntegerField(source='comment_set.count', read_only=True) # 댓글 갯수
    username = serializers.CharField(source='user.username', read_only=True)
    userImg = serializers.CharField(source='user.userImg',read_only=True)
    userpoint = serializers.IntegerField(source='user.point', read_only=True)
    
    class Meta:
        model = Review
        fields = ('id', 'title', 'content', 'created_at', 'updated_at','comment_set', 'comment_count', 'user','username',
                  'dislike_review_users_count', 'like_review_users_count','userImg','like_review_users','dislike_review_users',
                  'userpoint')
        read_only_fields = ('user','like_review_users','dislike_review_users')



        