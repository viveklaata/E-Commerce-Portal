from django.db import models

class Category(models.Model):
  name = models.CharField(max_length=100, blank=False)

  class Meta:
    ordering = ['name']
    verbose_name = 'Category'
    verbose_name_plural = 'Categories'

  def __unicode__(self):
    return self.name

  def __str__(self):
    return self.__unicode__()