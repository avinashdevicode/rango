from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from datetime import datetime
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        if self.views <0:
            self.views = 0
        if self.likes < 0: self.likes = 0
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)
        
    class Meta:
        verbose_name_plural = 'Categories'
    
    def __str__(self):
        return self.name
    
class Page(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    first_visit = models.DateTimeField(default=timezone.now, null=True)
    last_visit = models.DateTimeField(default=timezone.now, null=True)
    
    
    def __str__(self):
        return self.title
