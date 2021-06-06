from django.contrib import admin
from .models import Animes, Category, Comments

# Register your models here.
admin.site.register(Animes)
admin.site.register(Category)
admin.site.register(Comments)