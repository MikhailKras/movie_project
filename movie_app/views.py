from django.shortcuts import render, get_object_or_404
from django.db.models import F, Sum, Max, Min, Count, Avg, Value
from .models import Movie
# Create your views here.


def show_all_movie(request):
    # movies = Movie.objects.order_by(F('year').desc(nulls_first=True))
    movies = Movie.objects.annotate(
        true_bool=Value(True),
        false_bool=Value(False),
    )
    agg = movies.aggregate(Avg('budget'), Max('rating'), Min('rating'), Count('id'))
    for movie in movies:
        if not movie.slug:
            movie.save()
    data = {
        'movies': movies,
        'agg': agg,
    }
    return render(request, 'movie_app/all_movies.html', context=data)


def show_one_movie(request, slug_movie: str):
    movie = get_object_or_404(Movie, slug=slug_movie)
    data = {
        'movie': movie
    }
    return render(request, 'movie_app/one_movie.html', context=data)
