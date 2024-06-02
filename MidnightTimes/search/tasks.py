from celery import shared_task
from .models import KeywordSearch, NewsArticle
import requests
from django.conf import settings

api_key = settings.NEWS_API_KEY

@shared_task
def fetch_latest_news():
    keyword_searches = KeywordSearch.objects.all()
    for keyword_search in keyword_searches:
        last_searched = keyword_search.last_searched
        news_articles = fetch_news(keyword_search.keyword, last_searched)
        for article in news_articles:
            NewsArticle.objects.create(
                keyword_search=keyword_search,
                title=article['title'],
                description=article['description'],
                url=article['url'],
                published_at=article['publishedAt']
            )
        keyword_search.save()

def fetch_news(keyword, last_searched=None):
    url = f'https://newsapi.org/v2/everything?q={keyword}&apiKey={api_key}'
    if last_searched:
        url += f'&from={last_searched.isoformat()}'
    response = requests.get(url)
    return response.json().get('articles', [])
