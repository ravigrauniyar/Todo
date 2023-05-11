from django.contrib import admin

from .models import users, todo

admin.site.register(users)
admin.site.register(todo)