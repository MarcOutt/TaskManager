
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views import View
from .forms import UserCreationForm, UserLoginForm
from .models import CustomUser


class UserSignupView(View):
    def get(self, request):
        form = UserCreationForm()
        return render(request, 'user/user_signup.html', {'form': form})

    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  # Sauvegarde l'utilisateur créé par le formulaire
            username = form.cleaned_data.get('username')
            messages.success(request,
                             f'Bienvenue, {username} ! Votre compte a été créé avec succès. Vous pouvez maintenant vous connecter.')

            # Connexion automatique de l'utilisateur après la création du compte
            login(request, user)
            return redirect('home')  # Redirection vers une autre vue après l'inscription
        return render(request, 'user/user_signup.html', {'form': form})


class UserLoginView(View):
    """Permet d'afficher la page de connexion et le lien d'inscription"""
    template_name = 'user/user_login.html'
    form_class = UserLoginForm

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'],
                                password=form.cleaned_data['password'],
                                )
            print(user)
            if user is not None:
                login(request, user)
                return redirect('home')
        message = 'Identifiants invalides.'
        user = False
        return render(request, self.template_name, context={'form': form, 'message': message, 'user': user})


def user_logout(request):
    logout(request)
    messages.info(request, 'Vous avez été déconnecté avec succès.')
    return redirect('user_login')
