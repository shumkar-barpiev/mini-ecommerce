from django.urls import path
from . import views


app_name = 'ecommerce app'

urlpatterns = [
    path('', views.products_list, name='products_list'),
    path('login/', views.login, name='login'),
    path('login/myprofile', views.myprofile, name='myprofile'),
    path('<slug:category_slug>', views.products_list, name='products_by_category'),
    path('<int:id>/', views.product_detail, name='product_detail'),
]