from django.contrib import admin
from django.utils.html import format_html

from .models import *

@admin.register(Swiper)
class SliderAdmin(admin.ModelAdmin):

    def image_tag(self, obj):
        return format_html('<img src="{}" style="width: 480px; height: 180px;"/>'.format(obj.image.url))

    image_tag.short_description = 'bild'
    list_display = ['image_tag', 'title', 'text']