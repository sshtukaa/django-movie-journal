from django.contrib import admin
from .models import CustomUser, UserProfile, Movie, UserMovieRating

admin.site.register(CustomUser)
admin.site.register(Movie)
admin.site.register(UserProfile)
admin.site.register(UserMovieRating)
