from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import KeywordSearch, NewsArticle

admin.site.register(KeywordSearch)
admin.site.register(NewsArticle)
