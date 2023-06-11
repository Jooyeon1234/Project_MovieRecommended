from rest_framework import serializers, status
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse,HttpResponse

import requests
from django.shortcuts import get_object_or_404,get_list_or_404
from .serializers import MovieListSerializer,MovieSerializer,MovieCommentSerializer
from .models import Movie,MovieComment,Genre

from datetime import datetime


           
@api_view(['GET'])
def movie_list(request) :
    
    movies = get_list_or_404(Movie)
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request,movie_pk) : 
    if request.method == "GET" :
        movie = get_object_or_404(Movie, pk=movie_pk)
        serializer = MovieSerializer(movie)
        
        return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_likes(request,movie_pk) :
    if request.method == "POST" :
        movie = get_object_or_404(Movie,pk=movie_pk)
        
        if movie.like_users.filter(pk=request.user.pk).exists():
            movie.like_users.remove(request.user)
            is_liked = False
        else :
            movie.like_users.add(request.user)
            is_liked = True
        
        context = {
            'is_liked' : is_liked,
            'likes_count' : movie.like_users.count()
        }
        return JsonResponse(context)

@api_view(['GET'])
def movie_comment_list(request) :
    if request.method == "GET" :
        moviecomments = get_list_or_404(MovieComment)
        serializer = MovieCommentSerializer(moviecomments,many=True)
        return Response(serializer.data)

    
        
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def movie_comment_create(request,movie_pk) :


    if request.method == "POST" :
        movie = get_object_or_404(Movie, pk = movie_pk)
        
        if MovieComment.objects.filter(movie=movie, user=request.user).exists() :
            return JsonResponse({'error': '이미 댓글을 작성하셨습니다.'}, status=403)
        
        serializer = MovieCommentSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True) :
            serializer.save(movie = movie, user = request.user) # 해당 글에 댓글쓰기
            return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT', 'DELETE'])
def movie_comment_detail(request,movie_comment_pk) :
    moviecomment = get_object_or_404(MovieComment, pk=movie_comment_pk)

    if request.method == 'GET' :
        serializer = MovieCommentSerializer(moviecomment)
        return Response(serializer.data)
    
    elif not request.user.moviecomment_set.filter(pk=movie_comment_pk).exists():
        return Response({'detail': '권한이 없습니다.'}, status=status.HTTP_403_FORBIDDEN)
    
    elif request.method == 'PUT':
        serializer = MovieCommentSerializer(moviecomment, data=request.data)
        if serializer.is_valid(raise_exception=True) :
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE' :
        moviecomment.delete()
        return Response({ 'id': movie_comment_pk}, status=status.HTTP_204_NO_CONTENT)
        



@api_view(['GET'])
@permission_classes([IsAuthenticated])
def movie_recommendation(request):
    like_movies = request.user.like_movies.all()
    users = []
    genres = []
    for movie in like_movies:
        users += list(movie.like_users.all())
        genres += list(movie.genres.all())
    
    genre_set = set(genres)
    genre_list = list(genre_set)
    user_set = set(users)
    user_list = list(user_set)
    movies = []
    
    
    for user in user_list:
        movies += list(user.like_movies.exclude(id__in=like_movies).all())
    
    for genre in genre_list:
        movies += list(genre.movies.exclude(id__in=like_movies).all())
    
    movie_set = set(movies)
    movie_list = list(movie_set)
    movie_list.sort(key=lambda x: -x.like_users.count())
    movie_list = movie_list[:10]
    data = {
        'movies': [
            {
                'id' : movie.id,
                'title': movie.title,
                'overview': movie.overview,
                'poster_path': movie.poster_path,
                'vote_avg': movie.vote_avg,

            }
            for movie in movie_list
        ]
    }
    return JsonResponse(data)


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

@api_view(['GET'])
def movie_recommendation2(request):
    # 사용자가 좋아하는 영화들 가져오기
    like_movies = request.user.like_movies.all()

    # 모든 영화들 가져오기
    movies = Movie.objects.exclude(id__in=like_movies.values_list('id', flat=True))

    # TfidfVectorizer를 사용하여 overview 텍스트 벡터화
    vectorizer = TfidfVectorizer()

    # 추천 영화들을 담을 리스트
    recommendations = []

    # 사용자가 좋아하는 영화들과 유사한 다른 영화들을 추천
    for like_movie in like_movies:
        like_movie_overview = like_movie.overview

        # TfidfVectorizer를 사용하여 좋아하는 영화의 줄거리를 벡터화
        like_movie_vector = vectorizer.fit_transform([like_movie_overview])

        # 다른 영화들과의 코사인 유사도 계산
        similarity_scores = []
        for other_movie in movies:
            other_movie_overview = other_movie.overview

            # TfidfVectorizer를 사용하여 다른 영화의 줄거리를 벡터화
            other_movie_vector = vectorizer.transform([other_movie_overview])

            # 코사인 유사도 계산
            similarity_score = cosine_similarity(like_movie_vector, other_movie_vector)[0][0]
            similarity_scores.append((other_movie, similarity_score))

        # 유사도가 높은 순으로 정렬
        similarity_scores.sort(key=lambda x: x[1], reverse=True)
        

        # 추천 영화 선택
        recommended_movies = [score for score in similarity_scores[:15]]
        
        recommendations.extend(recommended_movies)

    # 중복된 추천 영화 제거
    recommendations.sort(key=lambda x: x[1], reverse=True)
    
    recommendations1 = []
    seen = set()

    for item in recommendations :
        if item[0] not in seen :
            recommendations1.append(item)
            seen.add(item[0])
    
    # recommendations1.sort(key=lambda x:x[1], reverse=True)
    
    recommendations = [recommended_movie[0] for recommended_movie in recommendations1[:15]]

    # 추천 영화들을 직렬화
    serializer = MovieListSerializer(instance=recommendations, many=True)
    serialized_recommendations = serializer.data

    # JSON 응답 반환
    return JsonResponse(serialized_recommendations, safe=False)


def movie_search(request,search_content,genre) :
    
    
    if search_content == 'all' :
        results_genre = Genre.objects.get(name=genre)
        results = Movie.objects.filter(genres = results_genre)

    elif genre =='all' : 
        results = Movie.objects.filter(title__contains= search_content)
    
    else :
        results_genre = Genre.objects.get(name=genre)
        results = Movie.objects.filter(title__contains= search_content, genres = results_genre)
    
    serializer = MovieSerializer(results,many=True)
    # data = {'movies' : list(results.values())}
    return JsonResponse(serializer.data, safe=False)
    




# @api_view(['GET', 'POST','PUT'])
# def takeGenre(request): 
#     if request.method == 'GET':
#         movieURL = f'https://api.themoviedb.org/3/discover/movie?api_key=f433951fa3f9ea7fc5b7f38dbec9ac20&language=ko-KR'
#         genreURL = f'https://api.themoviedb.org/3/genre/movie/list?api_key=f433951fa3f9ea7fc5b7f38dbec9ac20'
#         genreList = requests.get(genreURL).json()
#         movieList = requests.get(movieURL).json()
#         genre = genreList.get('genres')
        
#     return Response(genre)



