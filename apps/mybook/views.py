import json

from django.core import serializers
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from .models import *
from django.conf import settings
from django.core.paginator import *
from .task import *
from functools import wraps


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


def show_image(request):
    '''
    图片处理
    :param request: request
    :return: None
    '''
    return render(request, 'mybook/image01.html')


# 中间件
def show_exception(request):
    a = int('q')
    return HttpResponse("hello Exception")


# 上传图片
def upload_pic(request):
    return render(request, 'mybook/upload_pic.html')


def upload_handle(request):
    '''图片上传'''
    if request.method == "POST":
        pic = request.FILES.get('pic1', None)
        file_name = '%s/%s' % (settings.MEDIA_ROOT, pic.name)
        with open(file_name, 'wb') as f:
            # 字节，DEFAULT_CHUNK_SIZE = 64 * 2 ** 10
            for p in pic.chunks():
                f.write(p)
        return HttpResponse("ok")
    else:
        return HttpResponse("error")


# 分页
def show_page(request):
    '''接受前端传来的值：page为要显示的页数，pageSize为每页显示的数量'''
    page = request.GET.get('page')
    pageSize = int(request.GET.get('pageSize'))
    response = {}
    book_list = HeroInfo.objects.all()
    paginator = Paginator(book_list, pageSize)
    response['total'] = paginator.count
    try:
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)
    except EmptyPage:
        books = paginator.page(paginator.num_pages)
    response['list'] = json.loads(serializers.serialize("json", books))
    return JsonResponse(response)


# celery 异步
def celery_test(request):
    # 直接调用show()方法，执行比较耗时
    # show()
    # show.delay()这样调用，直接呈现效果，耗时任务交给另一个进程worker在后台执行
    show.delay()
    return HttpResponse('hello!!123')


# 登录验证

# 说明：这个装饰器的作用，就是在每个视图函数被调用时，都验证下有没法有登录，
# 如果有过登录，则可以执行新的视图函数，
# 否则没有登录则自动跳转到登录页面。
def check_login(f):
    @wraps(f)
    def inner(request, *arg, **kwargs):
        if request.session.get('is_login') == '1':
            return f(request, *arg, **kwargs)
        else:
            return redirect('/mybook/login/')

    return inner


def login(request):
    # 如果是POST请求，则说明是点击登录按扭 FORM表单跳转到此的，那么就要验证密码，并进行保存session
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username=username, password=password)
        print(user)
        if user:
            # 登录成功
            # 1，生成特殊字符串
            # 2，这个字符串当成key，此key在数据库的session表（在数据库存中一个表名是session的表）中对应一个value
            # 3，在响应中,用cookies保存这个key ,(即向浏览器写一个cookie,此cookies的值即是这个key特殊字符）
            request.session['is_login'] = '1'  # 这个session是用于后面访问每个页面（即调用每个视图函数时要用到，即判断是否已经登录，用此判断）
            # request.session['username']=username  # 这个要存储的session是用于后面，每个页面上要显示出来，登录状态的用户名用。
            # 说明：如果需要在页面上显示出来的用户信息太多（有时还有积分，姓名，年龄等信息），所以我们可以只用session保存user_id
            request.session['user_id'] = user[0].id
            return redirect('/mybook/index/')
    # 如果是GET请求，就说明是用户刚开始登录，使用URL直接进入登录页面的
    return render(request, 'mybook/login.html')


@check_login
def login_index(request):
    # students=Students.objects.all()  ## 说明，objects.all()返回的是二维数据表，即一个列表，里面包含多个元组
    # return render(request,'index.html',{"students_list":students})
    # username1=request.session.get('username')
    user_id1 = request.session.get('user_id')
    # 使用user_id去数据库中找到对应的user信息
    userobj = User.objects.filter(id=user_id1)
    print(userobj)
    if userobj:
        return render(request, 'mybook/index.html', {"user": userobj[0]})
    else:
        return render(request, 'mybook/index.html', {'user', '匿名用户'})
