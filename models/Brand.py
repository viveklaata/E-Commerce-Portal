from django.db import models

class Brand(models.Model):
  name = models.CharField(max_length=100, blank=False)

  class Meta:
    ordering = ['name']
    verbose_name = 'Brand'
    verbose_name_plural = 'Brands'

  def __unicode__(self):
    return self.name

  def __str__(self):
    return self.__unicode__()