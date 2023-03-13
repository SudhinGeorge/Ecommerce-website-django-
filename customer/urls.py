from . import views
from django.urls import path


urlpatterns = [
     path('registercustomer', views.registercustomer, name='registercustomer'),
     path('logout', views.logoutcustomer, name='logoutcustomer'),
     path('logincustomer', views.logincustomer, name='logincustomer'),
     path('products', views.homepage, name='products'),
     path('addtocart', views.addproducttocart, name='addtocart'),
     path('removefromcart', views.removeproductfromcart, name='removefromcart'),
     path('viewcustomercart', views.viewcustomercart, name='viewcustomercart'),
     path('removefromcartpage/<int:cart_item_id>', views.removeproductcartpage, name='removeproductcartpage'),
     ]