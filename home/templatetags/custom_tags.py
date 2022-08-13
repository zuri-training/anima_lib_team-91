from django import template
from django.urls import reverse

register = template.Library()

@register.simple_tag
def anchor(home, about_us):
    return reverse(home) + '#' + about_us