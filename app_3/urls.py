from django.urls import path
from .views import app_3, app_3_tool, app_3_api

urlpatterns = [
    path('', app_3, name='app_3'),
    path('tool', app_3_tool, name='app_3_tool'),
    path('api', app_3_api, name='app_3_api'),
]
