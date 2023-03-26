from django.urls import path
from . import views 
from art.controller import authview



urlpatterns = [
    path('',views.index,name='index'),
    path('contact',views.contact,name = 'contact'),
    path('category',views.category_list,name ='category'),
    path('products',views.product_list,name = 'products'),
    path('product_details/<slug>',views.product_details,name='product_details'),
    path('category_details/<slug>',views.category_details,name = 'category_details'),

    path('cart/add/<int:id>/', views.cart_add, name='cart_add'),
    path('cart/item_clear/<int:id>/', views.item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',views.item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',views.item_decrement, name='item_decrement'),
    path('cart/cart_clear/', views.cart_clear, name='cart_clear'),
    path('cart/cart-detail/',views.cart_detail,name='cart_detail'),

    path('register/',authview.register, name = 'register'),
    path('login/',authview.loginpage, name = 'loginpage'),
    path('logout/',authview.logoutpage, name ='logout'),

    path('wishlist/', views.wishlist, name='wishlist'),
    path('wishlist/add/<int:product_id>/', views.addwishlist, name='addwishlist'),
    path('wishlist/remove/<int:wishlist_id>/', views.removewishlist, name='removewishlist'),

    path('checkout/', views.checkout, name='checkout'),
    path('placeorder/',views.placeorder,name='placeorder'),
    path('thankyou/', views.thankyou, name='thankyou'),
    path('userprofile/',views.userprofile, name='userprofile'),
   
    

  
    path('verify_payment/',views.verify_payment,name='verify_payment'),
    

    #admin
    path('adminlogin/',views.admin_login, name='admin_login'),
    path('adminlogout/',views.adminlogout, name ='adminlogout'),
    path('adminhome',views.adminhome,name='adminhome'),
    path('adminproduct',views.adminproduct,name='adminproduct'),
    path('products/<int:product_id>/delete/', views.delete_product, name='delete_product'),
    path('products/<int:pk>/update/',views.update_product, name='update_product'),
    path('adminorder',views.adminorder,name='adminorder'),
    path('orderdelete/<int:order_id>/delete/', views.delete_order, name='delete_order'),
    path('adminorderdetail/<int:pk>/',views.adminorderdetail,name='adminorderdetail'),
    path('updatestatus/<int:pk>/',views.adminupdatestatus,name='adminupdatestatus'),
    path('addcategory',views.addcategory,name='addcategory'),
    path('addproduct',views.addproduct,name='addproduct'),
    path('viewcategory',views.viewcategory,name='viewcategory'),
    path('categories/<int:category_id>/delete/', views.delete_category, name='delete_category'),
    path('messages',views.adminmessages,name='adminmessages'),
    path('message/<int:id>/delete',views.messagedelete,name='messagedelete'),
    




]