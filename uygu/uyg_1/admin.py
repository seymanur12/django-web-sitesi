from django.contrib import admin

# Register your models here.  http://127.0.0.1:8000/admin/
from .models import *

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Profil)
admin.site.register(Takip)
admin.site.register(Takipci)


class CategoryAdmin(admin.ModelAdmin): 
    list_display = ['title', 'status']
    list_filter = ['status']

class ProductAdmin(admin.ModelAdmin): 
    list_play = ['title', 'category','price','amount' ,'image_tag']
    list_filter = [ 'category']
    
    readonly_field = ('image_tag',)
    
admin.site.register(Category,CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Images)
admin.site.register(Settingg)
class ProductImagesInline(admin.TabularInline): 
    model = Images  # Images modelinden
    extra = 4