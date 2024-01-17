from django.shortcuts import render
from .models import Section, Chapter

# Create your views here.


def app_2(request):
    sections = Section.objects.all()
    id = request.GET.get('id')
    if id:
        section = Section.objects.filter(id=id)[0]
        chapters = Chapter.objects.filter(headline_id=id)
        title = request.GET.get('title')
        if title:
            chapter = Chapter.objects.filter(title=title)[0]
        else:
            pass
    else:
        pass
    return render(request, 'app_2.html', locals())


