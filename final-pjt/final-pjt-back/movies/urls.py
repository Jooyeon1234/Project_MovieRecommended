from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.movie_list),
    path('<int:movie_pk>/',views.movie_detail),
    path('<int:movie_pk>/likes/',views.movie_likes),
    path('<int:movie_pk>/comments/',views.movie_comment_create),
    path('comments/',views.movie_comment_list),
    path('movie_comments/<int:movie_comment_pk>/',views.movie_comment_detail),
    path('recommended/',views.movie_recommendation),
    path('recommended2/',views.movie_recommendation2),
    path('search/<search_content>/<genre>/',views.movie_search),
    

    
]