from django.urls import path
from .views import search_view
from . import views

app_name = 'Webapp'
urlpatterns = [
    path('top/', views.top_page, name='top'),
    path('search_view/', views.search_view, name='search_view')
]