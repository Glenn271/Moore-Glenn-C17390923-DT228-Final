from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from world.models import Housing, UserFaves, Profile
from django.contrib.auth.models import User
from . import models
from django.contrib.gis.geos import Point


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! { username }')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    context = {}
    u = User.objects.get(username=request.user.username)
    p = Profile.objects.get(user=u)

    context['user_faves'] = UserFaves.objects.filter(user=p)
    return render(request, 'users/profile.html', context)


