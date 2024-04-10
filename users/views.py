from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from common.views import TitleMixin
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from users.models import User, Advertisement


class UserLoginView(TitleMixin, LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm
    title = 'Авторизация'

class UserRegistrationView(TitleMixin, SuccessMessageMixin, CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')
    success_message = 'Вы успешно зарегистрированы!'
    title = 'Регистрация'

class UserProfileView(TitleMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'
    title = 'Личный кабинет'

    def get_success_url(self):
        return reverse_lazy('users:profile', kwargs={'pk': self.request.user.pk})

from django.shortcuts import render, redirect
from django.views import View
from .forms import AdvertisementForm

class CreateAdvertisementView(TitleMixin,UpdateView):
    model = Advertisement
    form_class = AdvertisementForm
    template_name = 'users/profile.html'
    title = 'Личный кабинет'
    def get(self, request):
        form = AdvertisementForm()
        return render(request, 'users/create_advertisement.html', {'form': form})

    def post(self, request):
        form = AdvertisementForm(request.POST)
        if form.is_valid():
            advertisement = form.save(commit=False)
            advertisement.user = request.user
            advertisement.save()
            return redirect(reverse_lazy('users:profile', kwargs={'pk': request.user.pk}))
        return render(request, 'users/create_advertisement.html', {'form': form})
