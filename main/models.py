from django.db import models


class QuoteCategory(models.Model):
    title = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.title


class Quote(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=200)
    quote_category = models.ForeignKey(
        'QuoteCategory', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        if (len(self.quote) > 50):
            return self.quote[:50] + "..."
        return self.quote
