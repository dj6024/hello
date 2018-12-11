from django.db import models

# Create your models here.


# 轮播
class Basens(models.Model):
    img = models.CharField(max_length=100)


# cookin (不要)
class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)


# 用户－－tonken
class Users(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    token = models.CharField(max_length=256)

    class Meta:
        db_table = 'app_users'


# 第二排商品
class Coll(models.Model):
    coname = models.IntegerField()
    path1 = models.CharField(max_length=256)
    path2 = models.CharField(max_length=256)
    collimg = models.CharField(max_length=256)
    goodsimg = models.CharField(max_length=256)
    cityimg = models.CharField(max_length=256)
    send = models.CharField(max_length=256)
    msg = models.CharField(max_length=256)
    desc = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    price2 = models.DecimalField(max_digits=6, decimal_places=2)
    coll = models.IntegerField()
    productImg = models.CharField(max_length=256)


# # 底部右边的ｌｏｇ
class Log(models.Model):
    img = models.CharField(max_length=256)
    alt = models.CharField(max_length=256)


# 底部左边商品展示
class Goodlist(models.Model):
    nameid = models.CharField(max_length=256)
    path1 = models.CharField(max_length=256)
    path2 = models.CharField(max_length=256)
    goodsimg = models.CharField(max_length=256)
    cityimg = models.CharField(max_length=256)
    send = models.CharField(max_length=256)
    msg = models.CharField(max_length=256)
    desc = models.CharField(max_length=256)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    price2 = models.DecimalField(max_digits=6, decimal_places=2)
    coll = models.IntegerField()
    productImg = models.CharField(max_length=256)

#
# # 子类图片
# class Tom(models.Model):
#     img = models.CharField(max_length=256)
#     t_goodlist = models.ForeignKey(Goodlist)
#
#
# # 子类图片说明
# class Ment(models.Model):
#     tipc = models.CharField(max_length=256)
#     exp = models.CharField(max_length=256)
#     m_goodlist = models.ForeignKey(Goodlist)



