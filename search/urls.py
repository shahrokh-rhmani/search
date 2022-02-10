from django.urls import path
from .views import HomePage, SearchResultView




urlpatterns = [
    path('',  HomePage.as_view(), name='home'),
    path('search/', SearchResultView.as_view(), name='search'),

]
