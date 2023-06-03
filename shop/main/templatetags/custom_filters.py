
from django import template

register = template.Library()

@register.filter
def get_data_by_id(y_dict, y_object, *args, **kwargs):
    return y_dict.get(y_object.id)



@register.filter
def multiply(value, arg):
    try:
        return int(value) * int(arg)
    except (ValueError, TypeError):
        return ''

