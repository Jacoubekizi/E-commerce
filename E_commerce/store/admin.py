from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import *

# Register your models here.
class CustomerAdmin(ModelAdmin):
    list_display = ['user', 'name']

    fieldsets = (
        ('Add Customer',{'fields':['user', 'name'], 'classes':['wide']}),
    )
    search_fields = ['name',]

class ProductAdmin(ModelAdmin):

    list_display = ['name', 'price', 'digital', 'image']

    fieldsets = (
        ('Add name product', {'fields':['name'], 'classes':'wide'}),
        ('Add Details', {'fields':['price', 'digital', 'image'],'classes':['wide']}),
    )

    search_fields = ('name',)
    list_per_page = 10

class AdminOrder(ModelAdmin):
    list_display = ['customer', 'date_order', 'complete', 'transcation_id']
    
    readonly_fields = ['date_order']
    fieldsets = (
        ('Add Customer', {
            'fields':['customer'], 'classes':'wide'
        }),
        ('Details', {'fields':['date_order', 'complete', 'transcation_id'],
                     'classes':['wide']}),
    )
    list_filter = ['complete']

class AdminOrderItem(ModelAdmin):
    list_display = ['product', 'order', 'quantity', 'date_added']
    readonly_fields = ['date_added']
    fieldsets = (
        ('Add Product', {
            'fields':['product',], 'classes':'wide'
        }),
        ('Add Order', {
            'fields':['order'], 'classes':'wide'
        }),
        ('Details', {'fields':['quantity', 'date_added'],
                     'classes':['wide']}),
    )

class AdminShippingAdderss(ModelAdmin):
    list_display = ['customer', 'order', 'address', 'city', 'state', 'zipcode', 'data_added']
    readonly_fields = ['data_added']
    fieldsets = (
        ('Add Customer', {
            'fields':['customer'], 'classes':'wide'
        }),
        ('Add Order', {
            'fields': ['order'], 'classes':'wide'
        }),
        ('Details', {
            'fields':['address', 'city', 'state', 'zipcode', 'data_added']
        })
    )

class AdminPrand(ModelAdmin):
    list_display = ('name',)

    fieldsets = (
        ('Add name prand', {
            'fields':['name'], 'classes':'wide'
        }),
    )

class AdminProperties(ModelAdmin):

    list_display = ['product', 'company', 'processor', 'System_type', 'generation', 'instelled_RAM', 'storege', 'graphics_card', 'color']
    fieldsets = (
        ('Add Product', {
            'fields':['product'], 'classes':'wide'
        }),
        ('Add Prand', {
            'fields':['company'], 'classes':'wide'
        }),
        ('Add Details', {
            'fields':['processor', 'System_type', 'generation', 'instelled_RAM', 'storege', 'graphics_card', 'color'], 'classes':'wide'
        })
    )
admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, AdminOrder)
admin.site.register(OrderItem, AdminOrderItem)
admin.site.register(ShippingAddress, AdminShippingAdderss)
admin.site.register(Prand, AdminPrand)
admin.site.register(Properties, AdminProperties)