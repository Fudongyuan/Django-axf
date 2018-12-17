import hashlib

from django.http import JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse

from app.models import Wheel, Nav, MustBuy, Shop, MainShow, FoodTypes, Goods, User, Cart


def home(request):
    wheels = Wheel.objects.all()
    navs = Nav.get_all()
    mustbuys = MustBuy.get_all()
    shops = Shop.get_all()
    shop1 = shops[0:1][0]
    shop2_3 = shops[1:3]
    # print(shops)
    # print(shop1)
    mainshows = MainShow.get_all()
    data = {
        'wheels': wheels,
        'navs' : navs,
        'mustbuys':mustbuys,
        'shop1':shop1,
        'shop2_3':shop2_3,
        'shop3_7':shops[3:7],
        'shop7_11':shops[7:11],
        'mainshows':mainshows
    }
    return render(request, 'home.html', context=data)


def market(request):
    # # 默认选中热销帮
    # tid = '104749'
    # foodtypes = FoodTypes.objects.all().order_by('typesort')
    # data = {
    #     'foodtypes':foodtypes,
    #     'tid':tid,
    # }
    # return render(request,'market.html',context=data)
    return redirect(reverse("app:queryfood",args=('104749','0','0')))

def queryfood(request,tid='104749',cid='0',sortid='0'):
    # 类别
    foodtypes = FoodTypes.objects.all().order_by('typesort')
    #商品
    goods  = Goods.objects.filter(categoryid=tid)

    # 获取子类
    childtypenames = foodtypes.filter(typeid=tid)[0].childtypenames
    print(childtypenames)
    # 全部分类:0#酸奶乳酸菌:103537#牛奶豆浆:103538#面包蛋糕:103540
    ctypes = [ value.split(':')   for value in childtypenames.split('#')]


    # 子类过滤
    # cid = 0表示获取全部子类，也就是不需要对商品进一步过滤
    if cid != '0':
        goods = goods.filter(childcid=cid)

    # 排序
    if sortid == '1':
        goods = goods.order_by("productnum")
    elif sortid == '2':
        goods = goods.order_by('price')
    elif sortid == '3':
        goods = goods.order_by('-price')

    data = {
        'title':"闪购",
        'foodtypes': foodtypes,
        'goods': goods,
        'tid':tid,
        'cid':cid,
        'ctypes':ctypes,
    }
    return render(request, 'market.html', context=data)


def cart(request):
    uid = request.session.get('uid')
    carts = Cart.objects.filter(user_id=uid)
    # 总记录书
    total = carts.count()
    # 选中的记录书
    is_selected = carts.filter(is_selected=1).count()
    res = 1 if is_selected == total else 0
    return render(request,'cart.html',context={'carts':carts,
                                               'allselect': res,
                                               })


def mine(request):
    uid = request.session.get('uid')
    username = request.session.get('username')
    return render(request,'mine.html',context={'is_login':uid,'username':username})


def login(request):
    # print(request.META['HTTP_REFERER'])
    # targetUrl = request.META['HTTP_REFERER']
    if request.method == 'GET':
        return render(request,'login.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        password = hashlib.md5(password.encode('utf8')).hexdigest()
        res = User.objects.filter(username=username,password=password)

        # 用户存在
        if res.exists():
            # 记录用户信息到session
            request.session['uid'] = res[0].id
            request.session['username'] = username
            return redirect(reverse('app:mine'))
            # return redirect(request.META['HTTP_REFERER'])
            return redirect(targetUrl)
        else:
            return redirect(reverse('app:login'))



def logout(request):
    request.session.flush()
    return redirect(reverse('app:mine'))

# 将商品添加到购物车
def addCart(request):
    gid = request.GET.get('gid')

    #获取用户是否登录
    uid = request.session.get('uid')

    data = {
        'code': 0,
        'msg': 'ok',
    }
    if not uid:  #  用户未登录
        data['code'] = '-1'  #用户未登录
        data['msg'] = '用户未登录'
    else:

        # 查询购物车中是否由该商品，如果有，数量加1
        carts = Cart.objects.filter(goods_id=gid).filter(user_id=uid)
        if carts.exists():
            cart = carts.first()
            cart.num += 1
        else:
            # 没有则创建
            cart = Cart()
            cart.user_id = uid
            cart.goods_id = gid
            cart.num += 1
        cart.save()
        data['num'] = cart.num

    return JsonResponse(data)


def subCart(request):
    gid = request.GET.get('gid')

    # 获取用户是否登录
    uid = request.session.get('uid')

    data = {
        'code': 0,
        'msg': 'ok',
    }
    if not uid:  # 用户未登录
        data['code'] = '-1'  # 用户未登录
        data['msg'] = '用户未登录'
    else:

        # 查询购物车中是否由该商品，如果有，数量加1
        carts = Cart.objects.filter(goods_id=gid).filter(user_id=uid)
        if carts.exists():
            cart = carts.first()
            # cart.num += 1
            if cart.num == 1:
                cart.delete()
                data['num'] = 0
            else:
                cart.num -= 1
                data['num'] = cart.num
            cart.save()

        else:
            data['code'] = '-2'
            data['msg'] = '商品不存在'

    return JsonResponse(data)


def changestate(request):
    gid = request.GET.get('gid')
    is_selected = request.GET.get('is_selected')
    uid = request.session.get('uid')
    cart = Cart.objects.filter(goods_id=gid, user_id=uid)
    print(cart,gid,is_selected)
    data = {
        'code': 0,
        'msg': 'ok',

    }

    if cart.exists():
        # 取反原来的选择
        current = cart[0];
        current.is_selected = int(is_selected)
        current.save()
        data['is_selected'] = is_selected


    # 是否全选
    select_num = Cart.objects.filter(is_selected=1, user_id=uid).count()
    all_num = Cart.objects.filter(user_id=uid).count()

    data['all_select'] = 1 if all_num == select_num else 0


    return JsonResponse(data)

# 全选
def allselect(request):
    uid = request.session.get('uid')
    flag = request.GET.get('flag')
    # print(flag,type(flag))
    result = Cart.objects.filter(user_id=uid)
    if flag == 'false':
        result.update(is_selected=0)
    else:
        result.update(is_selected=1)

    data = {
        'code':0,
        'msg':'ok'
    }
    return JsonResponse(data)