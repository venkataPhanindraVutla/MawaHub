from django import template
from django.utils import timezone
import timeago

register = template.Library()

@register.filter
def to_timeago(time):
    return timeago.format(time, timezone.now())
