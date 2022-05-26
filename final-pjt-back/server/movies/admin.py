from django.contrib import admin
from .models import Movie
# Register your models here.

# admin.site.register(Movie)

class MoviesAdmin(admin.ModelAdmin):
    list_display = ('title', )

admin.site.register(Movie, MoviesAdmin)
