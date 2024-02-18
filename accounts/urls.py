from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    path('', views.home, name="home"),
    path('add_movie/', views.add_movie, name='add_movie'),
    path('movie_detail/<str:imdbID>/', views.movie_details, name='movie_detail'),
    path('mark_as_watched/<str:movie_id>/', views.mark_as_watched, name='mark_as_watched'),
    path('profile/', views.user_profile, name='profile'),
     path('dwm/<str:movie_id>/', views.del_mov, name='dwm'),
]
