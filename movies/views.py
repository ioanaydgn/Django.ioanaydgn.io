from django.shortcuts import render
from pip import main
from .models import Category,Movie

categories_list = ["Adventure" , "Horror" , "Drama" , "Sci-fi"]
movie_list = [
    {
        "id":1,
        "movie_name": "movie 1",
        "movie_descriptions": "movie 1 descriptions",
        "banner": "img1.jpeg",
        "main" : True
    },
    {
        "id":2,
        "movie_name": "movie 2",
        "movie_descriptions": "movie 2 descriptions",
        "banner": "2.jpeg",
        "main" : True

    },
    {
        "id":3,
        "movie_name": "movie 3",
        "movie_descriptions": "movie 3 descriptions",
        "banner": "3.jpeg",
        "main" : False
    },
    {
        "id":4,
        "movie_name": "movie 4",
        "movie_descriptions": "movie 4 descriptions",
        "banner": "4.jpeg",
        "main" : False
    },
    "movie 1",
    "movie 2",
    "movie 3",
    "movie 4"
]

def home(request):
    data = {
        "categories" : Category.objects.all(),
        "movies" : Movie.objects.filter(main=True)
    }
    return render(request, "index.html" ,data)

def movies(request):
    data = {
        "categories" : Category.objects.all(),
        "movies" : Movie.objects.all()
    }
    return render(request, "movies.html",data)

def movie_details(request,id):
    data = {
        'movie':Movie.objects.get(id=id)
    }
    return render(request, "details.html",data)
