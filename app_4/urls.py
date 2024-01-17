from django.urls import path
from .views import app_4

urlpatterns = [
    path('', app_4, name="app_4"),
]
