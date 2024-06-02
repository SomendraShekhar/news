from django.db import models
from django.contrib.auth.models import User

class KeywordSearch(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=255)
    last_searched = models.DateTimeField(auto_now=True)
    last_api_request = models.DateTimeField(null=True, blank=True)
    search_count = models.IntegerField(default=0) 

    def increment_search_count(self):
        self.search_count += 1
        self.save()

    def __str__(self):
        return f'{self.keyword} by {self.user}'

class NewsArticle(models.Model):
    keyword_search = models.ForeignKey(KeywordSearch,related_name='news_articles', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    url = models.URLField()
    published_at = models.DateTimeField()

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return self.title
