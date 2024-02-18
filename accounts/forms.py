from django import forms
from .models import CustomUser
from django.contrib.auth.forms import UserCreationForm
class SearchForm(forms.Form):
    search_query = forms.CharField(label='Search', max_length=100)
class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username',)