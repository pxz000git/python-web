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
    # get请求获取参数
    url('^get_test1/$', views.get_test1, name='get_test1'),
    url('^get_test2/$', views.get_test2, name='get_test2'),
    url('^get_test3/$', views.get_test3, name='get_test3'),
    # post请求获取参数
    url('^post_test1/$', views.post_test1, name='post_test1'),
    url('^post_test2/$', views.post_test2, name='post_test2'),
    # Cookie
    url('^cookie_test/$', views.cookie_test, name='cookie_test'),
    # 重定向
    url('^red_test1/$', views.red_test1, name='red_test1'),
    url('^red_test2/$', views.red_test2, name='red_test2'),
    # Session
    url('^session_test1/$', views.session_test1, name='session_test1'),
    url('^session_test2/$', views.session_test2, name='session_test2'),
    url('^session_test2_handle/$', views.session_test2_handle, name='session_test2_handle'),
    url('^session_test3/$', views.session_test3, name='session_test3'),
    # 静态文件
    url('^$', views.show_image),
    # 中间件
    url('^exception/$', views.show_exception),
    # 上传图片
    url('^upload/$', views.upload_pic),
    url('^upload_handle/$', views.upload_handle),
    # 分页
    url('^page/$', views.show_page)



]
