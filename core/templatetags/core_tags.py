from django import template
from textwrap import wrap

register = template.Library()


@register.filter()
def wrapper(number):
    return ' '.join(wrap(str(number), 4))


@register.filter()
def get_color(status):
    if status.lower() == "active":
        return "text-success"
    elif status.lower() == "inactive":
        return "text-info"
    elif status.lower() == "overdue":
        return "text-danger"
    else:
        return 'text-secondary'


@register.filter()
def convert_date(date):
    return date.strftime("%d/%m/%y")
