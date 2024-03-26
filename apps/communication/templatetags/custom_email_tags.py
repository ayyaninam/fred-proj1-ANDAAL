from django import template

register = template.Library()

@register.filter()
def getusernameuniquekey(value):
    print(value)
    try:
        return value.split('--')[0]
    except:
        return value
    