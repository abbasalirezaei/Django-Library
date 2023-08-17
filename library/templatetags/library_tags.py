from django import template
from library.models import Library

register = template.Library()

@register.filter
def reached_category_limit(book, user):
    return book.customer_reached_category_limit(user)