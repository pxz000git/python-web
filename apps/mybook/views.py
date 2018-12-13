from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import *


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
    '''post请求：展示连接的页面'''
    return render(request, 'mybook/post_test1.html')


def post_test2(request):
    '''post请求'''
    uname = request.POST['uname']
    upwd = request.POST['upwd']
    ugender = request.POST['ugender']
    uhobby = request.POST.getlist('uhobby')
    context = {'uname': uname, 'upwd': upwd, 'ugender': ugender, 'uhobby': uhobby, }
    # 默认就是跳转
    return render(request, 'mybook/post_test2.html', context)


# COOKIE
def cookie_test(request):
    cookie = request.COOKIES
    response = HttpResponse()
    if cookie.get('c'):
        response.write(cookie['c'])
    # response.set_cookie('c', 'abc')
    return response


# 重定向
def red_test1(request):
    a = request.GET.get('a')
    context = {'a': a}
    return redirect('/mybook/red_test2/', context)


def red_test2(request):
    # 重定向是两次请求，其请求的数据不在同一个域
    a1 = request.GET.get('a')
    # 默认就是跳转
    return HttpResponse("重定向过来的页面 %s" % a1)


# SESSION:状态保存
# 通过用户登录
def session_test1(request):
    # 从session取值
    uname = request.session.get('myname', '默认值')
    context = {'uname': uname}
    return render(request, 'mybook/session_test1.html', context)


def session_test2(req):
    return render(req, 'mybook/session_test2.html')


def session_test2_handle(req):
    uname = req.POST.get('uname', None)
    # 往session写值
    req.session['myname'] = uname
    return redirect("/mybook/session_test1/")


def session_test3(req):
    # 删除session
    del req.session['myname']
    return redirect("/mybook/session_test1/")
