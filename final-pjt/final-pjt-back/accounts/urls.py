from django.urls import path

from . import views



urlpatterns = [
    # path('signup/', views.signup),
    # path('api-token-auth/', obtain_jwt_token),
    path('profile/<username>/', views.profile),
    path('<int:user_pk>/follow/', views.follow),
    path('allusers/', views.all_users),
    

]
