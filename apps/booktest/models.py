from django.db import models

"""
    定义模型类
"""


# Create your models here.
class BookInfo(models.Model):
    btitle = models.CharField(max_length=20)
    bpub_date = models.DateTimeField()

    def __str__(self):
        return self.btitle
        # return self.btitle.encode('utf-8')


class HeroInfo(models.Model):
    hname = models.CharField(max_length=10)
    hgender = models.BooleanField()
    hcontent = models.CharField(max_length=1000)
    # 引用其他类
    hbook = models.ForeignKey(BookInfo, on_delete=False)

    def __str__(self):
        return self.hname