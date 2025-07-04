from django import template

register = template.Library()

@register.filter
def dict_key(d, key):
    try:
        return d.get(key, 0)
    except (AttributeError, TypeError):
        return ''
