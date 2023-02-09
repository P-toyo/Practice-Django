from django import template

register = template.Library()

@register.simple_tag
def replace(request, key, value):
    url_dict = request.GET.copy()
    url_dict[key] = value

    return url_dict.urlencode()