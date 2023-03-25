from django import template
import pytz

register = template.Library()

@register.filter
def localize_date(value, user_timezone):
    print(f"Value before filtering: {value}")
    print(f"User timezone: {user_timezone}")

    try:
        user_tz = pytz.timezone(user_timezone)
        localized_date = value.astimezone(user_tz)
    except (pytz.UnknownTimeZoneError, ValueError, AttributeError):
        localized_date = value

    print(f"Localized date: {localized_date}")

    return localized_date
