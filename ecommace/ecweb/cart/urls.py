from  django.urls import path
from  . import views

app_name='cart'
urlpatterns=[
    path('',views.cart_details,name="cart_detail"),
    path('add/<int:product_id>/', views.add_cart, name='add_cart'),
    path('', views._cart_id, name='fun'),
    path('remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
path('fuul_remove/<int:product_id>/', views.full_remove, name='full_remove'),

]