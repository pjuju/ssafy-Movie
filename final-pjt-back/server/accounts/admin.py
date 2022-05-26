from django.contrib import admin
from .models import User
# Register your models here.

# admin.site.register(Movie)

class UsersAdmin(admin.ModelAdmin):
    list_display = ('username', )

admin.site.register(User, UsersAdmin)