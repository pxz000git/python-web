#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author:Pxz
# @Time :2018/12/14 0014上午 11:08
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin


class middle_ware(MiddlewareMixin):
    def process_exception(request, response, exception):
        # return HttpResponse("abc")
        return HttpResponse(exception)
