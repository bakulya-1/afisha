"""
URL configuration for Afisha project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from movie_app import views


app_name = "movie_app"
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('movie_app.urls', namespace="movie_app")),
    path('api/v1/directors/', views.DirectorListView.as_view(), name='director-list'),
    path('api/v1/directors/<int:id>/', views.DirectorDetailView.as_view(), name='director-detail'),
    path('api/v1/movies/', views.MovieListView.as_view(), name='movie-list'),
    path('api/v1/movies/<int:id>/', views.MovieDetailView.as_view(), name='movie-detail'),
    path('api/v1/reviews/', views.ReviewListView.as_view(), name='review-list'),
    path('api/v1/reviews/<int:id>/', views.ReviewDetailView.as_view(), name='review-detail'),
]
