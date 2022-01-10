from django.urls import path
from .views import index, beauty_treatments


urlpatterns = [
    path('', index, name='home'),
    path('ueber-uns/', beauty_treatments, name='about'),
]