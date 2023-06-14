from django.contrib import admin
from ecomapp.models import Apple_Product
from ecomapp.models import Order


# Register your models here.
# define ModalAdminClass

class Apple_ProductAdminClass(admin.ModelAdmin):
    list_display=['name','cat','price','status']
    list_filter=['status','cat']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id','order_id','qty','pid','uid']




# class Apple_AcceseriseAdminClass(admin.ModelAdmin):
#     list_display=['name','cat','price','status']
#     list_filter=['status','cat']



admin.site.register(Apple_Product,Apple_ProductAdminClass)
admin.site.register(Order, OrderAdmin)

# admin.site.register(Apple_Acceserise,Apple_AcceseriseAdminClass)
admin.site.site_header='Apple Store Dashboard'