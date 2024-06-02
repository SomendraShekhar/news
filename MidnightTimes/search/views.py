import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import KeywordSearch, NewsArticle
from .forms import SearchForm
import requests
from django.utils import timezone

from django.conf import settings

api_key = settings.NEWS_API_KEY

@login_required
def search_news(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            keyword = form.cleaned_data['keyword']
            user = request.user
            keyword_search, created = KeywordSearch.objects.get_or_create(user=user, keyword=keyword)
            now = timezone.now()
            print(keyword_search.last_api_request,now)
            if keyword_search.last_api_request and now - keyword_search.last_api_request < datetime.timedelta(minutes=15):
                news_articles = keyword_search.news_articles.all()
                print(keyword_search.last_api_request)
            else:
                if not created:
                    last_searched = keyword_search.last_searched
                    news_articles = fetch_news(keyword, last_searched)
                else:
                    news_articles = fetch_news(keyword)
                    keyword_search.increment_search_count()
                    print(news_articles)
                for article in news_articles:
                    published_at = datetime.datetime.strptime(article['publishedAt'], "%Y-%m-%dT%H:%M:%SZ")
                    description = article['description'] if article['description'] else ''
                    NewsArticle.objects.create(
                        keyword_search=keyword_search,
                        title=article['title'],
                        description=description,
                        url=article['url'],
                        published_at=published_at
                    )
                keyword_search.last_api_request = timezone.now()
                keyword_search.save()
            return redirect('search_results', keyword_search.id)
    else:
        form = SearchForm()
    return render(request, 'search/search.html', {'form': form})

def fetch_news(keyword, last_searched=None):
    url = f'https://newsapi.org/v2/everything?q={keyword}&apiKey={api_key}'
    if last_searched:
        url += f'&from={last_searched.isoformat()}'
    response = requests.get(url)
    print(response)
    return response.json().get('articles', [])

@login_required
def search_results(request, keyword_search_id):
    keyword_search = KeywordSearch.objects.get(id=keyword_search_id, user=request.user)
    print(keyword_search)
    articles = keyword_search.news_articles.all()
    print(articles)
    return render(request, 'search/result.html', {'keyword_search': keyword_search, 'articles': articles})

@login_required
def search_history(request):
    keyword_searches = KeywordSearch.objects.filter(user=request.user).order_by('-last_searched')
    return render(request, 'search/history.html', {'keyword_searches': keyword_searches})
