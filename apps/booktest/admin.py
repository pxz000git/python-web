from django.contrib import admin
from .models import *

"""
    注册模型类
"""


class HeroInfoInline(admin.TabularInline):
    model = HeroInfo
    # 在添加一本图书的同时，可以关联添加3个英雄的信息
    extra = 3


class BookInfoAdmin(admin.ModelAdmin):
    # 列表页的显示效果
    list_display = ['id', 'btitle', 'bpub_date']
    # 根据字段过滤
    list_filter = ['btitle']
    search_fields = ['btitle']
    list_per_page = 10
    # 添加页，修改页属性
    fieldsets = [
        ('base', {'fields': ['btitle']}),
        ('super', {'fields': ['bpub_date']})
    ]

    inlines = [HeroInfoInline]


class HeroInfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'hname', 'hgender', 'hcontent', 'hbook']


# Register your models here.


# 注册到管理员中
admin.site.register(BookInfo, BookInfoAdmin)
admin.site.register(HeroInfo, HeroInfoAdmin)
