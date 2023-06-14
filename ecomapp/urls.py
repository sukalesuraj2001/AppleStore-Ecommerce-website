from django.urls import path
from ecomapp import views

urlpatterns = [
    
    path('', views.home),
    
    path('tv', views.tv),
    # path('register', views.register),
    # path('cart', views.cart),
    path('addproduct', views.addproduct),
    path('payment', views.payment),
    path('iphones/<ipv>', views.iphones),
    path('ipad/<iv>', views.ipad),
    path('watch/<wv>', views.watch),
    path('macbook/<mv>', views.macbook),
    path('macdesktop/<mdv>', views.macdesktop),
    path('acceserise', views.acceserise),
    path('about', views.about),
    # path('productlist/<pid>', views.productlist),
    path('productlist/<pid>', views.productlist),
    path('account', views.account),
    path('base', views.reuse),
    # path('sort/<sv>', views.sort),
    path('catfilter/<catv>', views.catfilter),
    # delete
    path('delproduct/<rid>',views.delproduct),
    path('editproduct/<rid>',views.editproduct),
    path('djangoform',views.djangoform),
    path('modelform',views.modelform),
    path('register',views.user_register),
    path('login',views.User_login),
    path('setsession',views.setsession),
    path('getsession',views.getsession),
    path('cart/<pid>',views.addtocart),
    path('logout',views.user_logout),
    path('viewcart',views.viewcart),
    path('changeqty/<pid>/<f>',views.changeqty),
    path('delcart/<pid>/<f>',views.changeqty),
    path('placeorder',views.placeorder),
    path('makepayment',views.makepayment),
    path('store',views.storedetails),



    
]
