from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import City
from django.db.models import Q



class HomePage(TemplateView):
    template_name = 'home.html'




class SearchResultView(ListView):
    model = City
    context_object_name = 'search_list'
    template_name = 'search.html'

    def get_queryset(self):
        query = self.request.GET.get('q')
        search_list = City.objects.filter(
            Q(name__icontains=query) | Q(country__icontains=query)
        )
        return search_list
