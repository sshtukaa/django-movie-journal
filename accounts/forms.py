from django import forms
from .models import CustomUser, UserMovieRating
from django.contrib.auth.forms import UserCreationForm
class SearchForm(forms.Form):
    SEARCH_CHOICES = [
        ('movie', 'Movie'),
        ('series', 'Series'),
        ('episode', 'Episode'),
    ]
    search_query = forms.CharField(label='Search by Title', required=False)
    year = forms.CharField(label='Search by year', required=False)
    search_type = forms.ChoiceField(label='Search Type', choices=SEARCH_CHOICES, required=False, widget=forms.RadioSelect)
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username',)
class RatingForm(forms.ModelForm):
    class Meta:
        model = UserMovieRating
        fields = ['rating']