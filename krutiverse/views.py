from django.shortcuts import render
from django.contrib.auth import login
import json
from authlib.integrations.django_client import OAuth
from django.conf import settings
from django.shortcuts import redirect, render, redirect
from django.urls import reverse
from urllib.parse import quote_plus, urlencode
from .forms import UserCreationForm


def home(request):
    return render(request, 'krutiverse/home.html')

def register(request):
    # if request.method == 'POST':
    #     # Process registration form
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         user = form.save()
    #         # Log the user in
    #         login(request, user)
    #         # Redirect to complete blood profile
    #         return redirect('profile')
    # else:
    #     form = UserCreationForm()
    return render(request, 'krutiverse/reg.html')

def profile(request):
    return render(request, 'krutiverse/profile.html')
    



  









# Registration View
