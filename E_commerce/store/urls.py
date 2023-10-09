from django.urls import path
from . import views

urlpatterns =[
    path('', views.Store, name='store'),
    path('cart/', views.Cart, name='cart'),
    path('checkout/', views.Checkout, name='checkout'),
    path('update_item/', views.updateItem, name='update_item'),
    path('process_order/', views.processOrder, name='process'),
    path('shopsigle/<int:pro_id>/', views.ShopSingle, name='shopsingle')
]