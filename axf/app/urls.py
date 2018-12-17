from django.conf.urls import url, include
from app import views

urlpatterns = [
    url(r'^home/$',views.home,name='home'),
    url(r'^market/$',views.market,name='market'),
    url(r'^queryfood/(\d+)/(\d+)/(\d+)/$',views.queryfood,name='queryfood'),
    url(r'^cart/$',views.cart,name='cart'),
    url(r'^mine/$',views.mine,name='mine'),

    # 登录
    url(r'^login/$',views.login,name='login'),
    url(r'^logout/$',views.logout,name='logout'),

    # 购物车
    url(r'^addcart/$',views.addCart,name='addcart'),
    url(r'^subcart/$',views.subCart,name='subcart'),
    url(r'^changestate/$',views.changestate,name='changestate'),
    url(r'^allselect/$',views.allselect,name='allselect'),
]
