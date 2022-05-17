from django.contrib import admin
from .models import Hero, Todo, User


admin.site.register(Hero)
admin.site.register(Todo)
admin.site.register(User)