from django.views.generic import ListView
from . models import QuoteCategory, Quote


class HomeView(ListView):
    template_name = "main/home.html"
    model = Quote

    def get_queryset(self):
        query_set = super().get_queryset()
        query_set = query_set.select_related('quote_category')

        return query_set.order_by('-created_at')
