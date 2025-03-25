from django import template
register = template.Library()

@register.filter
def get(list, index):
    try:
        return list[index]
    except:
        return None
    