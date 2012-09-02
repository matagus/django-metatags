# -*- coding: UTF-8 -*-
from django import template
from django.core.cache import cache

from metatags import app_settings, models

register = template.Library()

@register.inclusion_tag('metatags/meta_tags.html')
def meta(obj=None, meta={}):
    """
    Template tag to generate meta tags. Takes an optional parameter of a
    template object to pull the tags from. If not passed, it will return the
    default meta tags, as set in their respective templates.
    """
    try:
        cachename = 'metatags_%s_%s' % (obj.__class__.__name__, obj.id)
    except AttributeError:
        cachename = 'meta_default'

    metatags = cache.get(cachename)

    if not metatags and cachename != 'meta_default':
        try:
            metatags = models.MetaTag.objects.get(object_id=obj.id,
                content_type__app_label=obj._meta.app_label,
                content_type__model=obj._meta.module_name)
        except models.MetaTag.DoesNotExist:
            metatags = None

        if app_settings.METATAGS_CACHE_TTL:
            cache.set(cachename, metatags, app_settings.METATAGS_CACHE_TTL)

    return {"meta_tags": metatags}
