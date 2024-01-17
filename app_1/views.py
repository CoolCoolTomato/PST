from django.shortcuts import render
from .models import Titles, Contents
from django.core.paginator import Paginator
from django.core.paginator import PageNotAnInteger
from django.core.paginator import EmptyPage
# Create your views here.


def app_1(request, id):
    titles = Titles.objects.all()
    content_list = Contents.objects.filter(headline__id=id)
    return render(request, 'app_1.html', locals())
