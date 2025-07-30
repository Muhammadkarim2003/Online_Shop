from django.urls import path
from . import views


app_name = 'product'

urlpatterns = [
    path('', views.ProductListView.as_view(), name='index'),
    path('category/<int:pk>/', views.CategoryProductList.as_view(), name='category_products'),
    path('product_detail/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),

    path('cart_summary/', views.cart_summary, name='cart_summary'),
    path('cart_add/', views.cart_add, name='cart_add'),
    path('cart_update/', views.cart_update, name='cart_update'),
    path('cart_delete/', views.cart_delete, name='cart_delete'),
]



