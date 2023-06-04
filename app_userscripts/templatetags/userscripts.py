from django import template

from ..models import UserScripts

register = template.Library()


@register.simple_tag
def userscripts(position):
    scripts = UserScripts.objects.filter(active=True, position=position)
    response = ''
    for script in scripts:
        response += f'\n{script.script}\n'
    return response
