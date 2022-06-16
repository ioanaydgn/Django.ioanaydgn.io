from django.urls import path
from django.views import View
from . import views

# https://127.0.0.1:8000/
# https://127.0.0.1:8000/movies
# https://127.0.0.1:8000/movies/3
# https://127.0.0.1:8000/movies/family-guy

urlpatterns = [
    path("", views.home, name="home"),
    path("home", views.home),
    path("movies", views.movies, name="movies"),
    path("movies/<int:id>", views.movie_details, name="details"),
]
