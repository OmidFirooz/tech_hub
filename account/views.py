from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import ProfileUpdateForm

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            print(f"User created: {user.username}")
            login(request, user)
            return redirect('resources:homepage')
    else:
        form = UserCreationForm()
    return render(request, 'account/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('resources:homepage')
    else:
        form = AuthenticationForm()
    return render(request, 'account/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('resources:homepage')

@login_required
def profile_view(request):
    try:
        profile = request.user.profile
    except:
        print(f"Profile does not exist for user: {request.user.username}")
        return redirect('account:profile_update')
    return render(request, 'account/profile.html', {'profile': profile})

@login_required
def profile_update(request):
    if request.method == 'POST':
        form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if form.is_valid():
            form.save()
            return redirect('account:profile_view')
    else:
        form = ProfileUpdateForm(instance=request.user.profile)
    return render(request, 'account/profile_update.html', {'form': form})
