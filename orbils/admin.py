from django.contrib import admin
from django.utils.html import format_html

# Register your models here.
from .models import Contact , Courses , CartItem
admin.site.register(Contact)
admin.site.register(CartItem)

class CoursesAdmin(admin.ModelAdmin):
    list_display = ('coursename', 'shortdescription','display_image','category', 'original_price','discounted_price')
    search_fields = ('coursename', 'shortdescription','category')
    list_filter = ('category',)  # Add filters for 'created_at' field

    # readonly_fields = ['display_image']
    def display_image(self, obj):
        if obj.courseimg:
            return format_html('<img src="{}" style="max-height: 80px; max-width: 80px;border-radius:50%;" />', obj.courseimg.url)
        else:
            return 'No Image'

    display_image.short_description = 'Image'

admin.site.register(Courses, CoursesAdmin)