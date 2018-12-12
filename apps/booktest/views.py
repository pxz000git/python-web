from django.shortcuts import render
from django.http import request, response, HttpResponse
from django.template import RequestContext, loader
from .models import *


def index(request):
    # 在settings.py文件中TEMPLATES：'DIRS': [os.path.join(BASE_DIR, 'templates')]

    # temp = loader.get_template('booktest/index.html')
    # render(request, temp)
    # return HttpResponse("Hello World!!!")
    bookList = BookInfo.objects.all()

    context = {'list': bookList}
    return render(request=request, template_name='booktest/index.html', context=context)


def show(request,id):
    bookInfo = BookInfo.objects.get(pk=id)
    herolist = bookInfo.heroinfo_set.all()
    context = {'list': herolist}
    return render(request, 'booktest/show.html', context)
