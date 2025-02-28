from django.contrib import admin
from .models import Book, CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'published_date')
    search_fields = ('title', 'author')
    list_filter = ('publication_year')

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('username','email','date_of_birth', 'profile_photo','is_staff', 'is_active', 'is_superuser')
    search_fields = ("username",)
    ordering = ('username',)

admin.site.register(Book, BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)