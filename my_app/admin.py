from django.contrib import admin
from .models import Auth, Category, Item, BaseUser

# Register your models here.
admin.site.register(Auth)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(BaseUser)