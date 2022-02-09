from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import City



class HomePage(TemplateView):
    template_name = 'home.html'




class SearchResultView(ListView):
    model = City
    template_name = 'search.html'   
