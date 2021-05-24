from django.contrib import admin

from .models import Clothing, ClothingType, ShoppingSite, ClothingSex

admin.site.register(Clothing)
admin.site.register(ClothingType)
admin.site.register(ShoppingSite)
admin.site.register(ClothingSex)
