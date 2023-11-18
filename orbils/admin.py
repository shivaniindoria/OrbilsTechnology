from django.contrib import admin

# Register your models here.
from .models import Contact , Courses , CartItem
admin.site.register(Contact)
admin.site.register(Courses)
admin.site.register(CartItem)
