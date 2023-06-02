from django.db import models
from django.contrib.auth.models import AbstractUser




class User(AbstractUser):

    image = models.ImageField(upload_to='product_images', verbose_name='Изображение')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
