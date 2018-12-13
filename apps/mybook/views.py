from django.http import HttpResponse
from django.shortcuts import render
from .models import *


# Create your views here.


def index(request):
    return HttpResponse("Hello...")


def get_num(request, id):
    return HttpResponse(id)


def get_nums(request, p1, p2, p3):
    return HttpResponse('year:' + p1 + ', month:' + p3 + ', day:' + p2)


def detail(request):
    list = BookInfo.books2.all()
    context = {'list': list}
    return render(request, "mybook/detail.html", context)


def get_test1(request):
    '''展示连接的页面'''
    return render(request, 'mybook/get_test1.html')


def get_test2(request):
    '''接收一键一值'''
    # 接收值
    a1 = request.GET.get('a')
    b1 = request.GET['b']
    c1 = request.GET.get('c')
    # 构造上下文
    context = {'a': a1, 'b': b1, 'c': c1}
    # 向模板中传递上下文，并进行渲染
    return render(request, 'mybook/get_test2.html', context)


def get_test3(request):
    '''接收一键多值'''
    list = request.GET.getlist('a')
    context = {'keys': list}
    return render(request, 'mybook/get_test3.html', context)


def post_test1(request):
    '''展示连接的页面'''
    return render(request, 'mybook/post_test1.html')


def post_test2(request):
    '''接收一键一值'''
    uname = request.POST['uname']
    upwd = request.POST['upwd']
    ugender = request.POST['ugender']
    uhobby = request.POST.getlist('uhobby')
    context = {'uname': uname, 'upwd': upwd, 'ugender': ugender, 'uhobby': uhobby, }

    return render(request, 'mybook/post_test2.html', context)

