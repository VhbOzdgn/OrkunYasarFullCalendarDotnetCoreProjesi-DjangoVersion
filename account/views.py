from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required, user_passes_test
from account.models import AppUser
from .forms import UserRegisterForm, UserLoginForm
# Create your views here.

@login_required(login_url='login')
@user_passes_test(lambda u: u.role == AppUser.Roles.SECRETARY)
def register_view(request):
    form = UserRegisterForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        user.set_password(form.cleaned_data.get('password1'))
        user.save()
        return redirect('home:index')
    return render(request, 'pages/register.html', context={
        'form': form
    })


def login_view(request):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        remember_me = form.cleaned_data.get('remember_me')
        print(remember_me)
        user = authenticate(username=username, password=password)
        if user:
            logout(request)
            login(request, user)
            if not remember_me:
                request.session.set_expiry(0)
            return redirect('appointment:index')
    return render(request, 'pages/login.html', context={
        'form': form
    })


def logout_view(request):
    logout(request)
    return redirect('home:index')
