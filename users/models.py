from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    bio = models.TextField(blank=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True)

    REQUIRED_FIELDS = ['email']  # Здесь вы определяете требуемые поля для создания пользователя

    def __str__(self):
        return self.username
