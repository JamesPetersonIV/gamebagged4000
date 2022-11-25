from django.contrib import admin

from .models import *
#11/23/2022
# Register your models here.


#admin.site.register(Product)
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    #list on admin display
    list_display = ['name', 'slug', 'price']
    #prepopulate field
    prepopulated_fields = {'slug':('name',)}
    #edit list
    list_editable = ['price']

admin.site.register(OrderPro)
#@admin.register(OrderPro)
#class OrderProAdmin(admin.ModelAdmin):
    #list_display = ['customer', 'created_on', 'status']
    #set filter for list
    #list_editable = ['status']

admin.site.register(Tag)