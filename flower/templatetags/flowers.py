from django import template
from waterreminder.models import Reminder

register = template.Library()

@register.filter
def humanise(value):
    translator = dict(Reminder.REMINDER)
    return translator[value]
