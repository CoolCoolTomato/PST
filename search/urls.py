from django.urls import path
from .views import *

urlpatterns = [
    path('', MysearchView(), name='search')
]
