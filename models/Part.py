from django.db import models

class Part(models.Model):
  subcategory = models.ForeignKey('Subcategory', on_delete=models.CASCADE, related_name='parts')
  brand = models.ForeignKey('Brand', on_delete=models.CASCADE, related_name='parts')
  name = models.CharField(max_length=100, blank=False)

  class Meta:
    ordering = ['brand__name', 'name']
    verbose_name = 'Part'
    verbose_name_plural = 'Parts'

  def __unicode__(self):
    return self.brand.name+' '+self.name

  def __str__(self):
    return self.__unicode__()