from django.urls import path
from .views import app_2

urlpatterns = [
    path('', app_2, name='app_2'),
]
