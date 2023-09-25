from django import template

register = template.Library()

@register.filter
def get(dictionary, key):
    return dictionary.get(key, '')  # Provide a default value here if needed
