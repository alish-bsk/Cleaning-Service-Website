from django import template

register = template.Library()

@register.filter
def index(lst, i):
    """Return the element at position i in a list, safely."""
    try:
        return lst[i]
    except (IndexError, TypeError):
        return None
