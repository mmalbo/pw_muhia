from django import template
from pages.models import Pagina

register = template.Library()

@register.simple_tag
def get_page_list():
    pages = Pagina.objects.all()
    return pages

