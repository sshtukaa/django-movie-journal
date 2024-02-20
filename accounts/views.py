from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SearchForm, CustomUserCreationForm, RatingForm
from .models import Movie, UserProfile, UserMovieRating
from django.contrib.auth.decorators import login_required
from .helper import get_watched_movies, omdbresponse
import requests
def home(request):
    return render(request, 'index.html')
def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})
def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'registration/login.html', {'form': form})
@login_required
def add_movie(request):
    try:
        data = None
        if request.method == 'POST':
            form = SearchForm(request.POST)
            if form.is_valid():
                search_query = form.cleaned_data['search_query']
                year = form.cleaned_data.get('year', '')
                search_type = form.cleaned_data.get('search_type', 'movie')
                omdb_url = f"http://www.omdbapi.com/?apikey=400bc237&s={search_query}&type={search_type}"
                if year:
                    omdb_url += f'&y={year}'
                response = requests.get(omdb_url)
                data = response.json()
                if data['Response'] == 'True':
                    data['Search'] = sorted(data['Search'], key=lambda x: x['Year'])
        else:
            form = SearchForm()
        return render(request, 'add_movie.html', {'form': form, 'data': data, 'watched_movies': get_watched_movies(request.user, data)})
    except Exception as e:
        return redirect("add_movie")
@login_required
def mark_as_watched(request, movie_id):
    user = request.user
    try:
        movie = Movie.objects.get(movie_id=movie_id)
    except Movie.DoesNotExist:
        response = omdbresponse(movie_id, "i")
        if response.status_code == 200:
            movie_data = response.json()
            movie = Movie.objects.create(
                movie_id=movie_id,
                title=movie_data.get('Title'),
                year=movie_data.get('Year')
            )
        else:
            return render(request, 'error.html', {'message': 'Failed to fetch movie data from API'})
    user_profile = UserProfile.objects.get(user=user)
    user_profile.watched_movies.add(movie)
    user_profile.save()
    return redirect('add_movie')
@login_required
def movie_details(request, imdbID):
    user = request.user
    form = RatingForm(request.POST or None)
    try:
        rating = UserMovieRating.objects.get(user=user, movie_id=imdbID)
    except UserMovieRating.DoesNotExist:
        rating = None
    if request.method == 'POST' and form.is_valid():
        user_rating = form.cleaned_data['rating']
        if rating:
            rating.rating = user_rating
            rating.save()
        else:
            rating = UserMovieRating.objects.create(
                user=user,
                movie_id=imdbID,
                rating=user_rating
            )
    response = omdbresponse(imdbID, "i")
    movie_data = response.json()
    return render(request, 'movie_details.html', {'imdbID': imdbID, 'movie_data': movie_data, 'watched_movies': get_watched_movies(request.user, movie_data), 'rating': rating, 'form': form})
@login_required
def user_profile(request):
    user = request.user
    watched_movies = None
    user_profile = UserProfile.objects.get_or_create(user=user)[0]  # Создаем профиль пользователя, если его нет
    if user.is_authenticated:
        watched_movies = user_profile.watched_movies.all()
    is_watched = False
    if user.is_authenticated and watched_movies:
        if user.username in [movie.title for movie in watched_movies]:
            is_watched = True
    
    return render(request, 'user_profile.html', {'user': user, 'watched_movies': watched_movies})
@login_required
def del_mov(request, movie_id):
    user_profile = get_object_or_404(UserProfile, user=request.user)
    watched_movie = user_profile.watched_movies.filter(id=movie_id).first()
    if watched_movie:
        user_profile.watched_movies.remove(watched_movie)
        return redirect('profile')
    else:
        return render(request, 'error.html', {'message': 'Failed to delete movie from watched list.'})