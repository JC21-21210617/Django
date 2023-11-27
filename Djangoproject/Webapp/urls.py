from django.urls import path
from . import views

app_name = 'Webapp'
urlpatterns = [
    path('top/', views.top_page, name='top')
]