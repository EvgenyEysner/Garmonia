from django import template
from ..models import Swiper

register = template.Library()


@register.simple_tag()
def get_swiper_images():
    """
    Display Employees
    """
    return Swiper.objects.all()