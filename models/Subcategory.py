from django.db import models

class Subcategory(models.Model):
  category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='subcategories')
  name = models.CharField(max_length=100, blank=False)

  class Meta:
    ordering = ['category__name', 'name']
    verbose_name = 'Subcategory'
    verbose_name_plural = 'Subcategories'

  def __unicode__(self):
    return self.category.name+' / '+self.name

  def __str__(self):
    return self.__unicode__()