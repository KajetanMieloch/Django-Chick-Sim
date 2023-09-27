from django import template

register = template.Library()

@register.filter
def get(dictionary, key):
    return dictionary.get(key, '')  # Provide a default value here if needed

@register.filter
def mul(value, arg):
    return float(value) * float(arg)

@register.filter
def pow(value, arg):
    return float(value) ** float(arg)

@register.filter
def dev(value, arg):
    return float(value)/float(arg)

@register.filter
def round(value):
    return int(value)