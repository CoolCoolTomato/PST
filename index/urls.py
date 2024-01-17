from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('notice/<int:id>', notice, name='notice'),
    path('feedback/', feedback, name='feedback'),
    path('support/', support, name='support'),
    path('topic/', topic, name='topic'),
    path('tool/', tool,  name='tool'),
]
