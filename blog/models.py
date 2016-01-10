from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(unique=True, max_length=255)
    content = models.TextField()
    category = models.ForeignKey('blog.Category')

    class Meta:
        ordering = ['-pub_date']

    def __unicode__(self):
        return '%s' % self.title

    def get_absolute_url(self):
        return "/%s/%s/%s/" % (self.pub_date.year, self.pub_date.month, self.slug)

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField(max_length=100, db_index=True)

    def __unicode__(self):
        return '%s' % self.name

    def get_absolute_url(self):
        return "/category/%s/" % (self.slug)
