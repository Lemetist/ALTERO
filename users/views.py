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

from django.views.generic import CreateView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from .forms import AdvertisementForm
from .models import Advertisement

class CreateAdvertisementView(CreateView):
    model = Advertisement
    form_class = AdvertisementForm
    template_name = 'users/create_advertisement.html'

    def form_valid(self, form):
        print("Форма действительна. Обработка POST-запроса...")
        advertisement = form.save(commit=False)
        advertisement.user = self.request.user
        advertisement.save()
        print("Объявление успешно сохранено в базу данных.")
        return redirect(reverse_lazy('users:profile', kwargs={'pk': self.request.user.pk}))

    def form_invalid(self, form):
        print("Форма недействительна. Ошибки формы:", form.errors)
        return super().form_invalid(form)


