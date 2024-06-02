from django.urls import path
from . import views

urlpatterns = [
    path('manage_users/', views.manage_users, name='manage_users'),
    path('block_user/<int:user_id>/', views.block_user, name='block_user'),
    path('set_quota/<int:user_id>/', views.set_quota, name='set_quota'),
    path('trending_keywords/', views.trending_keywords, name='trending_keywords'),
]
