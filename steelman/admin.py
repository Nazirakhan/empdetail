from django.contrib import admin
from .models import empdata
from django.utils.html import format_html

class empAdmin(admin.ModelAdmin):
    list_display = ("name","company","designation","joined_date","display_image","country")

    def display_image(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="50" height="50" />'.format(obj.photo.url))
        else:
            return "No Image"
        
    display_image.short_description = 'Preview'


admin.site.register(empdata, empAdmin)
