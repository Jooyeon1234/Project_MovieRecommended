from rest_framework import serializers
from django.contrib.auth import get_user_model
from movies.serializers import MovieSerializer
from movies.serializers import MovieCommentSerializer



class UserSerializer(serializers.ModelSerializer):
    
    moviecomment_set = MovieCommentSerializer(many=True)
    like_movies = MovieSerializer(many=True)    
    followings_count = serializers.IntegerField(source='followings.count',read_only=True)
    followers_count = serializers.IntegerField(source='followers.count',read_only=True)
    

    class Meta:
        model = get_user_model()
        fields = ('id','username','email','last_name','first_name','like_movies','like_reviews','dislike_reviews','followings','followers','followings_count','followers_count','point','userImg','moviecomment_set')

    