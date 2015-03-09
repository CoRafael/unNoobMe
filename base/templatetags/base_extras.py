from django import template

register = template.Library()

@register.simple_tag
def activetag(request, urls):
    print "comparing " + request.path + " with " + urls
    if not request:
        return ""
    return "active" if request.path == urls else ""