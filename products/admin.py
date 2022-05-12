from django.contrib import admin

from products.models import ProductCategory, Product, Basket

# Register your models here.

admin.site.register(ProductCategory)

admin.site.register(Basket)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity', 'category')  # показ указанных полей в админ панели
    fields = ('name', 'image', 'description', 'short_description', ('price', 'quantity'),
              'category')  # обьединение некоторых полей
    readonly_fields = ('short_description',)  # режим тольок чтения для краткого описания
    ordering = ('name',)  # порядок выведения товаров по алфавиту
    search_fields = ('name',)  # поиск товаров по имени


class BasketAdminInLine(admin.TabularInline):
    model = Basket
    fields = ('product', 'quantity', 'created_timestamp')
    readonly_fields = ('created_timestamp',)
    extra = 0
