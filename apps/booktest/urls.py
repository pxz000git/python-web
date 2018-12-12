#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Author:Pxz
# @Time :18-12-11下午6:37


from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(\d+)$', views.show),
]
