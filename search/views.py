from django.shortcuts import render
from django.core.paginator import *
from django.conf import settings
from haystack.views import SearchView
from app_1.models import Contents
from app_2.models import Chapter
from app_3.models import Content
from app_4.models import Section

# Create your views here.


class MysearchView(SearchView):
    template = 'search.html'

    def create_response(self):
        if not self.request.GET.get('q', ''):
            res = "什么也没找到"
            return render(self.request, self.template, locals())
        else:
            qs = super(MysearchView, self).create_response()
            #  读源码，折阳寿
            #  print(self.get_context().get('page').__dict__.get('object_list')[0].__dict__)
            return qs

