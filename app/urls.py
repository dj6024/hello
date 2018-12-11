from django.conf.urls import url

from app import views

urlpatterns = [
    url(r'^$', views.index, name='index'),

    # 注册
    url(r'^register/$', views.register, name='register'),
    # 尚品详情页
    url(r'^goodsinfo/(\d+)/$', views.goodsinfo, name='goodsinfo'),
    # 登录
    url(r'^logon/$', views.logon, name='logon'),
    # 退出
    url(r'^logou/$', views.logou, name='logou'),
    # 购物车
    url(r'^cart/$', views.cart, name='cart')
    # 验证用户是否存在
    # url(r'^checkname/$', views.checkname, name='checkname'),
]