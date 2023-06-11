from rest_framework import serializers
from .models import Movie,Genre,MovieComment
from django.db.models import Avg

class GenreListSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Genre
        fields = '__all__'

class MovieListSerializer(serializers.ModelSerializer):
    
    genres = GenreListSerializer(many=True)
    class Meta:
        model = Movie
        fields = '__all__'

class MovieCommentSerializer(serializers.ModelSerializer) :

    username = serializers.CharField(source='user.username', read_only=True)
    userImg = serializers.CharField(source='user.userImg', read_only=True)
    movie = MovieListSerializer(read_only=True)
    userpoint = serializers.IntegerField(source='user.point',read_only=True)

    class Meta :
        model = MovieComment
        fields = ('id','content','movie', 'created_at', 'updated_at', 'user','username','vote_detail', 'userImg','userpoint')
        read_only_fields = ('user',)


class MovieSerializer(serializers.ModelSerializer) : 
    like_users_count = serializers.IntegerField(source="like_users.count", read_only= True)
    genres = GenreListSerializer(many=True)
    
    moviecomment_set = MovieCommentSerializer(many=True,read_only=True)
    moviecomment_count = serializers.IntegerField(source="moviecomment_set.count",read_only=True)
    
    average_vote_detail = serializers.SerializerMethodField()
    
    def get_average_vote_detail(self, obj):
        if obj.moviecomment_set.count() == 0:
            return None
        else:
            return round(obj.moviecomment_set.aggregate(Avg('vote_detail'))['vote_detail__avg'],1)

    

    class Meta :
        model = Movie
        fields = '__all__'
