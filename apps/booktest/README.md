##创建项目
    django-admin startproject test1
##创建应用
    python manage.py startapp booktest
##向settings文件中注册应用
        INSTALLED_APPS= [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
        'apps.booktest',
    ]
##生成迁移(根据定义的模型类生成和选择的数据库特定的sql语句)
    python manage.py makemigrations
##执行迁移(根据生成的迁移文件去数据库中执行特定的sql语句来创建表)
    python manage.py migrate
##进入shell:
    python manage.py shell
    正常的shell操作：
        b = BookInfo()
        b.btitle = 'abc'(btitle,这里的btitle和类中的字段必须一样,才能映射,但不是调用类中的字段，类中字段只是和数据库生成有关)
        from datetime import datetime
        b.bpub_date = datetime(year=1990,month=1,day=12)
        b.save()
    时区警告,在settings中修改:TIME_ZONE = 'Asia/Shanghai'
    RuntimeWarning: DateTimeField BookInfo.bpub_date received a naive datetime (1990-01-12 00:00:00) while time zone support is active.
    查看信息：
        BookInfo.objects.all(),调用了类的__str__()方法
    创建管理员：
        python manage.py createsuperuser
    管理页面改为中文:
        LANGUAGE_CODE = 'zh-hans'
    在admin中看到自己定义的模型类：
        需要在admin中注册应用模型
            打开admin.py，注册模型
            from django.contrib import admin
            from .models import BookInfo
    自定义管理页面:
        Django提供了admin.ModelAdmin类
        通过定义ModelAdmin的子类，来定义模型在Admin界面的显示方式
        class QuestionAdmin(admin.ModelAdmin):
            ...
        admin.site.register(Question, QuestionAdmin)
        列表页属性
            list_display：显示字段，可以点击列头进行排序
            list_display = ['pk', 'btitle', 'bpub_date']

            list_filter：过滤字段，过滤框会出现在右侧
            list_filter = ['btitle']

            search_fields：搜索字段，搜索框会出现在上侧
            search_fields = ['btitle']

            list_per_page：分页，分页框会出现在下侧
            list_per_page = 10
        添加、修改页属性
            fields：属性的先后顺序
            fields = ['bpub_date', 'btitle']

            fieldsets：属性分组
            fieldsets = [
                ('basic',{'fields': ['btitle']}),
                ('more', {'fields': ['bpub_date']}),
            ]
        关联对象
            对于HeroInfo模型类，有两种注册方式

        方式一：与BookInfo模型类相同
        方式二：关联注册
        按照BookInfor的注册方式完成HeroInfo的注册

        接下来实现关联注册
            from django.contrib import admin
            from models import BookInfo,HeroInfo

            class HeroInfoInline(admin.StackedInline):
                model = HeroInfo
                extra = 2

            class BookInfoAdmin(admin.ModelAdmin):
                inlines = [HeroInfoInline]

            admin.site.register(BookInfo, BookInfoAdmin)
            可以将内嵌的方式改为表格
            class HeroInfoInline(admin.TabularInline)
        布尔值的显示
            发布性别的显示不是一个直观的结果，可以使用方法进行封装
            def gender(self):
                if self.hgender:
                    return '男'
                else:
                    return '女'
            gender.short_description = '性别'
            在admin注册中使用gender代替hgender
            class HeroInfoAdmin(admin.ModelAdmin):
                list_display = ['id', 'hname', 'gender', 'hcontent']
##视图：
    一般在应用app下建urls.py，作为路由，在test1.urls.py中分发到应用app下的url.py,然后指定到目标视图
##模板：
    在settings.py文件中TEMPLATES：'DIRS': [os.path.join(BASE_DIR, 'templates')],
    在项目目录下建目录templates,再在该目录下创建应用的文件，在不同应用文件下创建应用自身的html模板文件
    视图/index.html:如：booktest/index.html
##数据返回：
    bookList = BookInfo.objects.all()
    context = {'list': bookList}