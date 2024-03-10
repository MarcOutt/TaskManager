from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import UserCreationForm, UserLoginForm


class UserSignupView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'user/user_signup.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Bienvenue, {username} ! Votre compte a été créé avec succès. Vous pouvez maintenant vous connecter.')
            return redirect('user_login')
        return render(request, 'user/user_signup.html', {'form': form})


class UserLoginView(View):
    def get(self, request):
        form = UserLoginForm()
        return render(request, 'user/user_login.html', {'form': form})

    def post(self, request):
        form = UserLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('user_profile')
            else:
                messages.error(request, 'Identifiants incorrects. Veuillez réessayer.')
        return render(request, 'user/user_login.html', {'form': form})


def user_logout(request):
    logout(request)
    messages.info(request, 'Vous avez été déconnecté avec succès.')
    return redirect('user_login')
