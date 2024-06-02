from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from search.models import KeywordSearch
from django.db import models

@user_passes_test(lambda u: u.is_superuser)
def manage_users(request):
    users = User.objects.all()
    return render(request, 'admin_panel/manage_users.html', {'users': users})

@user_passes_test(lambda u: u.is_superuser)
def block_user(request, user_id):
    user = User.objects.get(id=user_id)
    user.is_active = False
    user.save()
    return redirect('manage_users')

@user_passes_test(lambda u: u.is_superuser)
def set_quota(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        quota = request.POST.get('quota')
        user.profile.quota = quota
        user.profile.save()
        return redirect('manage_users')
    return render(request, 'admin_panel/set_quota.html', {'user': user})

@user_passes_test(lambda u: u.is_superuser)
def trending_keywords(request):
    keywords = KeywordSearch.objects.values('keyword').annotate(count=models.Sum('search_count')).order_by('-count')[:10]
    return render(request, 'admin_panel/trending_keywords.html', {'keywords': keywords})
