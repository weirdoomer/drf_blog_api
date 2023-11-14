from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from PIL import Image


class User(AbstractUser):
    is_verified_email = models.BooleanField(default=False)


class Profile(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
        )
    bio = models.CharField(max_length=280, blank=True)
    avatar = models.ImageField(
        default='default_user.png', upload_to='profile_imgs'
        )
    is_author = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} profile'

    def save(self, *args, **kwargs):
        img = Image.open(self.avatar.path)

        max_size = (300, 300)

        if img.height > 300 or img.width > 300:
            img.thumbnail(max_size)
            img.save(self.avatar.path)

        super().save(*args, **kwargs)
