#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author:Pxz
# @Time :2018/12/12 0012下午 6:10

from django.conf.urls import url
from . import views

urlpatterns = [
    url('^index$', views.index),
    url('^(\d+)$', views.get_num),
    # 通过正则表达式组获取位置参数和关键字参数
    url(r'^(?P<p3>\d+)/(?P<p1>\d+)/(?P<p2>\d+)', views.get_nums, name='index'),
    url('^detail$', views.detail, name='detail'),

    url('^get_test1/$', views.get_test1, name='get_test1'),
    url('^get_test2/$', views.get_test2, name='get_test2'),
    url('^get_test3/$', views.get_test3, name='get_test3'),

    url('^post_test1/$', views.post_test1, name='post_test1'),
    url('^post_test2/$', views.post_test2, name='post_test2'),

]
