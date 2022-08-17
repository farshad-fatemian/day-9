from django.contrib import admin

from .models import Product , Comments , Picture

# Register your models here.

class commentinline(admin.StackedInline):
    model = Comments
    
class PictureInline(admin.StackedInline):
    model = Picture
    
class ProductAdmin(admin.ModelAdmin):
    inlines = [PictureInline,commentinline]


admin.site.register(Product,ProductAdmin)
admin.site.register(Comments)