from django.urls import path
from . import views

urlpatterns = [
    path('', views.search_news, name='search_news'),
    path('results/<int:keyword_search_id>/', views.search_results, name='search_results'),
    path('history/', views.search_history, name='search_history'),
]
