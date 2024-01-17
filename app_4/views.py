from django.shortcuts import render
from .models import Chapter, Section

# Create your views here.


def app_4(request):
    chapters = Chapter.objects.all()
    sections = Section.objects.all()
    s = request.GET.get('s')
    if s:
        section = Section.objects.get(section=s)
    else:
        pass
    return render(request, 'app_4.html', locals())

