from django.contrib import admin

from .models import ProductCategory, Product, Cart, CartItem


class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(ProductCategory)


class ProductsAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'quantity', 'image', 'slug')
    list_filter = ('category',)
    search_fields = ('name', )
    prepopulated_fields = {'slug': ('name',)}
    list_editable = ('price', 'quantity')


admin.site.register(Product, ProductsAdmin)


class CartAdmin(admin.ModelAdmin):
    list_display = ('user', 'order_date', 'status', 'issue_code', 'total_sum')
    list_filter = ('status', 'order_date')
    search_fields = ('user__email', 'user__first_name', 'user__last_name', 'issue_code')
    readonly_fields = ('order_date', 'total_sum')

    fieldsets = (
        (None, {
            'fields': ('user', 'order_date', 'status', 'issue_code', 'total_sum')
        }),
    )


admin.site.register(Cart, CartAdmin)


class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity')
    list_filter = ('cart__status', 'product')
    search_fields = ('cart__user__email', 'cart__user__first_name', 'cart__user__last_name', 'product__name')


admin.site.register(CartItem, CartItemAdmin)

