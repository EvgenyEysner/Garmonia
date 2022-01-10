from django import template
from ..models import Swiper, Carousel

register = template.Library()


@register.simple_tag()
def get_swiper_images():
    """
    Display Employees
    """
    return Swiper.objects.all()


@register.simple_tag()
def get_carousel_images():
    """
    Display Beauty Experts
    """
    return Carousel.objects.all()