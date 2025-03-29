from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager


class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given email, other_fields and password.
        """
        if not email:
            raise ValueError('User must have an email')
        user = self.model(email=self.normalize_email(email), password=password, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email, other_fields and password.
        """
        user = self.create_user(email, password=password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractUser):
    bio = models.TextField(max_length=256)
    profile_picture = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    followers = models.ManyToManyField(symmetrical=False)
    email = models.EmailField(verbose_name="email address", unique=True, max_length=255)
    username = models.TextField(max_length=256)


    def __str__(self):
        return self.username
    
    objects = CustomUserManager()
    USERNAME_FIELD = 'email'

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)