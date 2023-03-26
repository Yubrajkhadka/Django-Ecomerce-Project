from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Category)
class AdminCategory(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
   
@admin.register(Contact)
class AdminContact(admin.ModelAdmin):
    list_display = ['name','email','subject','message']
    
   
@admin.register(Product)
class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'is_available', 'created_date', 'modified_date']
    list_filter = ['is_available', 'created_date', 'modified_date']
    list_editable = ['price', 'stock', 'is_available']
    prepopulated_fields = {'slug': ('name',)}
    search_fields =['name','price','stock']




class OrderItemInline(admin.TabularInline):
    model = OrderItem
    


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    inlines = [OrderItemInline]
    list_display = ['user','firstname','lastname','phone','email','address','payment_method','amount','paid','date']
    search_fields =['firstname','payment_method']
    list_filter = ['firstname', 'payment_method']

@admin.register(Admin)
class AdminU(admin.ModelAdmin):
    list_display = ['user','full_name','mobile']


    



