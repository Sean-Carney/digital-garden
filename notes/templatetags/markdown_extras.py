from django import template
from django.template.defaultfilters import stringfilter

import markdown as md

register = template.Library()

@register.filter()
@stringfilter
def markdown(value):
	return md.markdown(value, extensions=['markdown.extensions.extra', 'markdown.extensions.admonition', 'markdown.extensions.toc', 'markdown.extensions.wikilinks'])

@register.filter()
@stringfilter
def toc(value):
	temp = md.Markdown(extensions=['toc'])
	temp.convert(value)
	return temp.toc
