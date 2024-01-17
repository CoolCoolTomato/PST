from django.shortcuts import render, redirect
from .models import Notice
from .form import FeedbackModelForm
from django.contrib import messages
#  工具包
from .tools.base_ed import *
from .tools.md5_e import *
from .tools.url_ed import *
from .tools.hex_ascii_c import *
from .tools.hill_ed import *
from .tools.ord_ascii_c import *
from .tools.hex_utf8_c import *
# Create your views here.


#  首页
def index(request):
    return render(request, 'index.html')


#  公告
def notice(request, id):
    notices = Notice.objects.all().order_by('-id')
    if id == 0:
        id = notices[0].id
    content = Notice.objects.filter(id=id)[0]
    return render(request, 'notice.html', locals())


#  反馈
def feedback(request):
    if request.method == 'POST':
        form = FeedbackModelForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "提交成功，感谢您的支持")
        else:
            messages.warning(request, "提交失败，内容不能为空")
        return redirect('/feedback')
    return render(request, 'feedback.html')


#  留着以后恰钱
def support(request):
    return render(request, 'support.html')


#  工具
def tool(request):
    t = request.GET.get('tool')
    if request.method == 'POST':
        if t == "base85":
            s = request.POST['encode_text']
            m = request.POST['tool_mode']
            res = base85_ed(s, m)
        elif t == "base64":
            s = request.POST['encode_text']
            m = request.POST['tool_mode']
            res = base64_ed(s, m)
        elif t == "base32":
            s = request.POST['encode_text']
            m = request.POST['tool_mode']
            res = base32_ed(s, m)
        elif t == "base16":
            s = request.POST['encode_text']
            m = request.POST['tool_mode']
            res = base16_ed(s, m)
        elif t == "url":
            s = request.POST['encode_text']
            m = request.POST['tool_mode']
            res = url_ed(s, m)
        elif t == "md5":
            s = request.POST['encode_text']
            res = md5_e(s)
        elif t == "hex_ascii":
            s = request.POST['encode_text']
            m = request.POST['tool_mode']
            res = hex_ascii_c(s, m)
        elif t == "ord_ascii":
            s = request.POST['encode_text']
            m = request.POST['tool_mode']
            res = ord_ascii_c(s, m)
        elif t == "hex_utf8":
            s = request.POST['encode_text']
            m = request.POST['tool_mode']
            res = hex_utf8(s, m)
        elif t == "hill":
            s = request.POST['encode_text']
            m1 = request.POST['tool_mode_1']
            m2 = request.POST['tool_mode_2']
            k = request.POST['s_key']
            res = hill_ed(s, m1, m2, k)
        else:
            pass
    return render(request, 'tool.html', locals())


#  刷题网站
def topic(request):
    return render(request, 'topic.html')
