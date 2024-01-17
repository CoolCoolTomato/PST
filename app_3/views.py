from django.shortcuts import render
from .models import Mode, Title, Content

# Create your views here.


def app_3(request):
    id = request.GET.get('id')
    way = request.GET.get('way')
    #  有id，显示内容
    if id:
        mode = Mode.objects.filter(id=id)[0]
        titels = Title.objects.filter(mode__id=id)
        title = request.GET.get('title')
        if title:
            contents = Content.objects.filter(title__title=title)
        else:
            pass
    #  有way，显示方法
    elif way:
        the_way = Mode.objects.filter(id=way)[0].way
    #  默认状态为爬虫模块首页
    else:
        modes = Mode.objects.all()
    return render(request, 'app_3.html', locals())


def app_3_tool(request):
    return render(request, 'app_3_tool.html')


def app_3_api(request):
    return render(request, 'app_3_api.html')

