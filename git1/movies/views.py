from django.shortcuts import render
from .models import MovieData
from .serializers import MovieDataSerializer
from rest_framework import viewsets
from django.core.paginator import Paginator

# Create your views here.

def movie_info(request):
    movie_list = MovieData.objects.all()

    mov_name = request.GET.get("movie_name")
    if mov_name != "" and mov_name is not None:
        movie_list = movie_list.filter(name__icontains=mov_name)

    paginator = Paginator(movie_list, 1)
    page = request.GET.get("page")
    movie_list = paginator.get_page(page)

    return render(request, "movies/movie_info.html", {"movie_list": movie_list})

class MovieList(viewsets.ModelViewSet):
    queryset = MovieData.objects.all()
    serializer_class = MovieDataSerializer


class ActionMovies(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(category="action")
    serializer_class = MovieDataSerializer


class ComedyMovies(viewsets.ModelViewSet):
    queryset = MovieData.objects.filter(category="comedy")
    serializer_class = MovieDataSerializer
