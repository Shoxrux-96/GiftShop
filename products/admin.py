from django.contrib import admin
from .models import Category,Product,Customer,Order,mashxur
# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id','title','soni']
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','category','discount','size','status']
    list_filter = ['name','price','category','discount','size']
    
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name','last_name','phone','email']
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['product','customer','quantity','address','phone','date']
    radio_fields = {'color': admin.HORIZONTAL}

@admin.register(mashxur)
class mashxurAdmin(admin.ModelAdmin):
    list_display = ['nomi','image','chegirma']