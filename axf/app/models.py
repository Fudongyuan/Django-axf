from django.db import models

# 公共父类
class BaseModel(models.Model):
    trackid = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    img = models.CharField(max_length=200)

    @classmethod
    def get_all(cls):
        return cls.objects.all()

    class Meta:
        abstract = True

class Wheel(BaseModel):

    class Meta:
        db_table = 'axf_wheel'
class Nav(BaseModel):
    class Meta:
        db_table = 'axf_nav'
class MustBuy(BaseModel):
    class Meta:
        db_table = 'axf_mustbuy'

class Shop(BaseModel):
    class Meta:
        db_table = 'axf_shop'

# 主要信息
"""
insert into axf_mainshow(trackid,name,img,
categoryid,brandname,img1,childcid1,productid1,longname1,price1,marketprice1,
img2,childcid2,productid2,longname2,price2,marketprice2,
img3,childcid3,productid3,longname3,price3,marketprice3) 
"103532","爱鲜蜂","http://img01.bqstatic.com/upload/goods/201/701/1916/20170119164159_996462.jpg@200w_200h_90Q","103533",
"118824","爱鲜蜂·特小凤西瓜1.5-2.5kg/粒","25.80","25.8","http://img01.bqstatic.com/upload/goods/201/611/1617/20161116173544_219028.jpg@200w_200h_90Q","103534","116950","蜂觅·越南直采红心火龙果350-450g/盒","15.3","15.8","http://img01.bqstatic.com/upload/goods/201/701/1916/20170119164119_550363.jpg@200w_200h_90Q","103533","118826","爱鲜蜂·海南千
禧果400-450g/盒","9.9","13.8");
"""
class MainShow(BaseModel):
    categoryid = models.CharField(max_length=10)
    brandname = models.CharField(max_length=1000)
    img1 = models.CharField(max_length=200)
    childcid1 = models.CharField(max_length=10)
    productid1 = models.CharField(max_length=20)
    longname1 = models.CharField(max_length=200)
    price1 = models.FloatField()
    marketprice1 = models.FloatField()
    img2 = models.CharField(max_length=200)
    childcid2 = models.CharField(max_length=10)
    productid2 = models.CharField(max_length=20)
    longname2 = models.CharField(max_length=200)
    price2 = models.FloatField()
    marketprice2 = models.FloatField()
    img3 = models.CharField(max_length=200)
    childcid3 = models.CharField(max_length=10)
    productid3 = models.CharField(max_length=20)
    longname3 = models.CharField(max_length=200)
    price3 = models.FloatField()
    marketprice3 = models.FloatField()

    class Meta:
        db_table = 'axf_mainshow'

class FoodTypes(models.Model):
    typeid = models.CharField(max_length=10)
    typename = models.CharField(max_length=100)
    childtypenames = models.CharField(max_length=200)
    typesort = models.IntegerField()

    class Meta:
        db_table = 'axf_foodtypes'

"""
insert into axf_goods(productid,productimg,productname,
productlongname,isxf,pmdesc,specifics,price,marketprice,categoryid,
childcid,childcidname,dealerid,storenums,productnum) 
values("11951","http://img01.bqstatic.com/upload/goods/000/001/1951/0000011951_63930.jpg@200w_200h_90Q","","乐吧薯片鲜虾味50.0g",0,0,"50g",2.00,2.500000,103541,103543,"膨化食品","4858",200,4);
商品表：
商品id(productid)        118826  
图片(productimg)      http://img01.bqstatic.com/upload/goods/201/701/1916/20170119164119_550363.jpg@200w_200h_90Q
名字(productname)    爱鲜蜂·海南千禧果
长名字(productlongname)   爱鲜蜂·海南千禧果400-450g/盒
是否精选(isxf)    1
是否买一增一(pmdesc)   1
规格(specifics) 
价格(price)         13.80
原价(marketprice)     13.8
商品组id(categoryid)       103532
商品子组id(childcid)      103533
商品子组名名称(childcidname)   国产水果
详情页id(dealerid)       4858
库存(storenums)     7
销量(productnum) 

"""
class Goods(models.Model):
    productid = models.CharField(max_length=10)
    productimg = models.CharField(max_length=200)
    productname = models.CharField(max_length=100)
    productlongname = models.CharField(max_length=200)
    isxf = models.IntegerField()
    pmdesc = models.IntegerField()
    specifics = models.CharField(max_length=40)
    price = models.FloatField()
    marketprice = models.FloatField()
    categoryid = models.CharField(max_length=10)
    childcid = models.CharField(max_length=20)
    childcidname = models.CharField(max_length=200)
    dealerid = models.CharField(max_length=20)
    storenums = models.IntegerField()
    productnum = models.IntegerField()

    class Meta:
        db_table = 'axf_goods'

# 用户
class User(models.Model):
    username = models.CharField(max_length=60,unique=True)
    password = models.CharField(max_length=60)
    portrait = models.CharField(max_length=200,null=True)
    email = models.CharField(max_length=200,null=True)
    rank = models.CharField(max_length=20,null=True)
    # True表示男,false表示女
    sex = models.NullBooleanField(default=True,null=True)
    isdeleted = models.NullBooleanField(default=False,null=True)

    class Meta:
        db_table = 'axf_user'

# 购物车
class Cart(models.Model):
    """
    商品id
    用户id
    商品数量

    """
    goods = models.ForeignKey(Goods)
    user = models.ForeignKey(User)
    num = models.IntegerField(default=0)
    is_selected = models.IntegerField(default=0)
    class Meta:
        db_table = 'axf_cart'

class OrderModel(models.Model):
    orderno = models.CharField(max_length=128)
    user = models.ForeignKey(User)
    createtime = models.DateTimeField(auto_now=True)
    status = models.IntegerField(default=0)

    class Meta:
        db_table = 'axf_order'

class OrderGoods(models.Model):
    order = models.ForeignKey(OrderModel,default=None)
    goods = models.ForeignKey(Goods)
    num = models.IntegerField(default=1)

    class Meta:
        db_table = 'axf_ordergoods'