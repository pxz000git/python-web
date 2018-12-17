from django.db import models


class BookInfoManager(models.Manager):
    """
        自定义了管理器,使用了filter，更改了查询的结果集
    """

    def get_queryset(self):
        '''
        重写了get_queryset，意为查询会走这个方法，
        这里增加了过滤方法
        :return:
        '''
        return super(BookInfoManager, self).get_queryset().filter(isDelete=False)

    def create(self, btitle, bpub_date):
        '''
        方案二：
        创建模型类
        推荐方案：
        在管理器中增加一个对象的方法
        :param btitle:
        :param bpub_date:
        :return:
        '''
        b = BookInfo()
        b.btitle = btitle
        b.bpub_date = bpub_date
        b.bread = 0
        b.bcommet = 0
        b.isDelete = False
        return b


class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()
    bread = models.IntegerField(default=0)
    bcommet = models.IntegerField(default=0)
    isDelete = models.BooleanField(default=False)

    def __str__(self):
        return self.btitle

    class Meta:
        db_table = 'bookinfo'

    @classmethod
    def create(cls, btitle, bpub_date):
        '''
        方案一：
        创建模型类
        在模型类中增加一个类方法
        :param btitle:
        :param bpub_date:
        :return:
        '''
        b = BookInfo()
        b.btitle = btitle
        b.bpub_date = bpub_date
        b.bread = 0
        b.bcommet = 0
        b.isDelete = False
        return b

    # 当定义模型类时没有指定管理器，则Django会为模型类提供一个名为objects的管理器
    # 创建了两个管理器
    books1 = models.Manager()
    books2 = BookInfoManager()


class HeroInfo(models.Model):
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=True)
    isDelete = models.BooleanField(default=False)
    hcontent = models.CharField(max_length=100)
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)

    def __str__(self):
        return self.hname


class User(models.Model):
    username = models.CharField(max_length=16)
    password = models.CharField(max_length=32)
