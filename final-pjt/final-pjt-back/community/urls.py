from django.urls import path
from . import views



urlpatterns = [
    path('review/', views.review_list_create),
    path('review/<int:review_pk>/', views.review_detail),
    path('review/comments/',views.comment_list),
    path('comments/<int:comment_pk>/',views.comment_detail),
    path('review/<int:review_pk>/comments/',views.comment_create),
    path('<int:review_pk>/likes/',views.review_likes),
    path('<int:review_pk>/dislikes/',views.review_dislikes),
]