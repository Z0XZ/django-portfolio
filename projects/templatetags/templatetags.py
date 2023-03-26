from django import template
from django.utils import timezone

register = template.Library()

@register.filter
def seconds_since_updated(last_updated):
    delta = timezone.now() - last_updated
    return int(delta.total_seconds())
