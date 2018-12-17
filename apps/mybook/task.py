#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author:Pxz
# @Time :2018/12/17 0017上午 10:38

import time
from celery import task


@task
def show():
    '''
    模拟任务执行长的视图
    @task把这个函数作为celery的一个任务
    '''
    print("Hello...")
    time.sleep(10)
    print("World...")
