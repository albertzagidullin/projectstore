from django.urls import path

from products.views import products, about_me, basket_add, basket_delete

app_name = 'products'

urlpatterns = [
    path('', products, name='index'),
    path('<int:category_id>/', products, name='category'),  # фильтрация товаров по категориям
    path('page<int:page>/', products, name='page'),
    path('about_me/', about_me, name='about_me'),
    path('basket-add/<int:product_id>/', basket_add, name='basket_add'),
    path('basket-delete/<int:id>/', basket_delete, name='basket_delete'),
]
