from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    publication_year = models.IntegerField()

    class meta:
        Permissions =[
            ("can_view", "can view book"),
            ("can_create", "can create book"),
            ("can_edit", "can edit book"),
            ("can_delete", "can delete book"),
        ]

    def __str__(self):
        return self.title
    

   
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        """
        Creates and saves a User with the given username, date of
        birth and password.
        """
        if not email:
            raise ValueError("Users must have an email")
        user = self.model(email=self.normalize_email(email), password=password, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(email, password=password, **extra_fields)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
# Default user model with a custom user model that includes additional fields and functionality
class CustomUser(AbstractUser):
    date_of_birth = models.DateField(null=True)
    profile_photo = models.ImageField(upload_to="profile_photos/", blank=True, null=True)
    email = models.EmailField(verbose_name="email address", unique=True, max_length=255)

    def __str__(self):
        return self.username
    
    objects = CustomUserManager()
    USERNAME_FIELD = "email"