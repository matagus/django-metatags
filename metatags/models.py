from django.contrib.contenttypes import generic
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.translation import ugettext_lazy as _

class MetaTag(models.Model):
    """
    A set of data to be inserted into meta tags. Can be generically linked to
    other content types using contrib.contenttypes.GenericForeignKey.
    """
    content_type = models.ForeignKey(ContentType)
    object_id = models.PositiveIntegerField(db_index=True)
    content_object = generic.GenericForeignKey('content_type', 'object_id')
    keywords = models.CharField(_('Keywords'),
        max_length=500,
        blank=True,
        null=False,
        help_text=(
            'A comma-separated list of keywords relevant to the content of '
            'the page. Maximum length 500 characters, please keep under 15 '
            'unique keywords'
        )
    )
    description = models.TextField(_('Description'),
        max_length=250,
        blank=True,
        null=False,
        help_text=(
            'A short description of the content of the page. If left blank, '
            'will use the site-wide default. Maximum 250 characters, please '
            'keep under 200 characters.'
        )
    )
    index = models.BooleanField(_('Allow indexing?'),
        default=True,
        help_text=(
            'If checked, tells search engines that they are allowed to index '
            'the content of the page.'
        )
    )
    archive = models.BooleanField(_('Allow archival?'),
        default=True,
        help_text=(
            'If checked, tells search engines that they are allowed to store '
            'a full copy of the page&#39;s content.'
        )
    )
    snippet = models.BooleanField(_('Allow snippet?'),
        default=True,
        help_text=(
            'If checked, tells search engines that they are allowed to show '
            'snippets of the page&#39;s content alongside search results.'
        )
    )
    follow = models.BooleanField(_('Follow links?'),
        default=True,
        help_text=(
            'If checked, tells search engines that they are allowed to follow '
            'and index documents linked to from this page. There is usually no '
            'reason to uncheck this.'
        )
    )
    
    @property
    def robots(self, robots=[]):
        """
        Generates the content of the <meta type="robots" /> tag, which is 
        amalgamation of several fields.
        """
        props = {
            'index': self.index,
            'archive': self.archive,
            'follow': self.follow,
            'snippet': self.snippet
        }
        for key, value in props.items():
            if value:
                robots.append(key)
            else:
                robots.append('no%s' % key)
        return ','.join(robots)
    
    class Meta:
        unique_together = (('content_type', 'object_id'),)
        verbose_name = _('meta tag')
        verbose_name_plural = _('meta tags')
    
    def __unicode__(self):
        return 'Meta tags for %s "%s"' % (self.content_type, self.content_object,)
