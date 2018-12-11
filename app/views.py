import hashlib
import random
import time

from django.http import JsonResponse
from django.shortcuts import render, redirect


# Create your views here.
from app.models import Basens, Log, Goodlist, Coll, Users


# 如果报save错误，极大可能是包导入系统的数据库，就是包导错了
# 首页
def index(request):
    # data = {}
    wheel = Basens.objects.all()
    logs = Log.objects.all()
    goods = Goodlist.objects.all()
    colls = Coll.objects.all()
    # data['wheel'] = wheel
    # data['goods'] = goods
    # data['logs'] = logs
    # data['colls'] = colls
    #
    # data['username'] = user.username
    # username = request.session.get('username')

    token = request.session.get('token')
    if token:
        user = Users.objects.get(token=token)
        return render(request, 'index.html', context={'username': user.username, 'wheel': wheel, 'logs': logs, 'goods': goods, 'colls': colls})
    else:
        return render(request, 'index.html')
    # wheel = Basens.objects.all()
    # logs = Log.objects.all()
    # goods = Goodlist.objects.all()
    # colls = Coll.objects.all()
    # data['wheel'] = wheel
    # data['goods'] = goods
    # data['logs'] = logs
    # data['colls'] = colls
    # data['username'] = username
    # data = {
    #     'username': username,
    #     'wheel': wheel,
    #     'logs': logs,
    #     'goods': goods,
    #     'colls': colls
    # }
    # return render(request, 'index.html', context=data)


# 商品详情页
def goodsinfo(request, nameid):
    com = Goodlist.objects.filter(nameid=nameid)
    # print(com)
    tom = com.all()[0]
    return render(request, 'goodsinfo.html', context={'tom': tom})


# tonken 函数
def generate_token():
    token = str(time.time()) + str(random.random())
    md5 = hashlib.md5()
    md5.update(token.encode('utf-8'))
    return md5.hexdigest()


# 密码加密
def genereate_pd(password):
    sha = hashlib.md5()
    sha.update(password.encode('utf-8'))
    return sha.hexdigest()


# 注册
def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(password, username, 11111111111111)

        user = Users()
        user.username = username
        # user.password = password
        user.password = genereate_pd(password)
        user.token = generate_token()
        user.save()

        request.session['token'] = user.token
        response = redirect('app:index')
        # response.set_cookie('username', username)
        request.session['username'] = username
        request.session.set_expiry(60 * 60 * 1)

        return response


# 登录
def logon(request):

    if request.method == 'GET': # 获取页面
        return render(request, 'login.html')
    elif request.method == 'POST':  # 登录操作
        username = request.POST.get('username')
        password = genereate_pd(request.POST.get('password'))
        print(username, password,11111111111111111111111)

        users = Users.objects.filter(username=username).filter(password=password)
        if users.count():   # 成功
            response = redirect('app:index')
            # response.set_cookie('username', username, max_age=60*60*24*1)
            # request.session['username'] = username

            # 更新用户ｔｏｋｅｎ
            user = users.first()
            user.token = generate_token()
            user.save()
            request.session['token'] = user.token
            request.session.set_expiry(60*10)
            return response
        else:   # 失败
            return render(request, 'login.html', context={'err': '用户名或密码错误'})


# 退出登录
def logou(request):
    response = redirect('app:index')
    # response.delete_cookie('username')
    request.session.flush()
    return response


# 验证唯一性
# def checkname(request):
#     username = request.GET.get('username')
#     users = Users.objects.filter(username=username)
#     if users.exists():
#         return JsonResponse({'msg': '账号已存在', 'status': 0})
#     else:
#         return JsonResponse({'msg': '账号可以用', 'status': 1})
#     # print(username)

    # return JsonResponse({'msg': '账号可以用'})


#  购物车
def cart(request):
    return render(request, 'cart.html')
