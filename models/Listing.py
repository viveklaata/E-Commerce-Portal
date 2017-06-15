from django.db import models
from Portal.helpers import get_listing_image_upload_path

class Listing(models.Model):
  CONDITION_CHOICES = (
    ('N', 'New'),
    ('U', 'Used')
  )

  STATUS_CHOICES = (
    ('A', 'Active'),
    ('P', 'Pending'),
    ('S', 'Sold/Deleted'),
    ('E', 'Expired')
  )

  code = models.CharField(max_length=6, unique=True)
  part = models.ForeignKey('Part', on_delete=models.CASCADE, related_name='listings', blank=True, null=True)
  status = models.CharField(max_length=1, default='P', choices=STATUS_CHOICES)
  added_on = models.DateTimeField('Added On', auto_now_add=True)
  last_modified_on = models.DateTimeField('Last Modified On', auto_now=True)

  title = models.CharField(max_length=100, blank=True, null=True)
  subtitle = models.CharField(max_length=100, blank=True, null=True)
  description = models.TextField(max_length=5000, blank=True, null=True)
  price = models.CharField(max_length=100)
  condition = models.CharField(max_length=1, default='N', choices=CONDITION_CHOICES)
  location = models.CharField(max_length=100, blank=True, null=True)
  contact_info = models.CharField(max_length=100, blank=True, null=True)
  email = models.EmailField(blank=True, null=True)

  photo_1 = models.ImageField(upload_to=get_listing_image_upload_path, blank=True, null=True)
  photo_2 = models.ImageField(upload_to=get_listing_image_upload_path, blank=True, null=True)
  photo_3 = models.ImageField(upload_to=get_listing_image_upload_path, blank=True, null=True)
  photo_4 = models.ImageField(upload_to=get_listing_image_upload_path, blank=True, null=True)

  class Meta:
    ordering = ['-added_on']
    verbose_name = 'Listing'
    verbose_name_plural = 'Listings'

  def __unicode__(self):
    if len(self.title) > 0:
      return self.title
    else:
      return '(No title) '+str(self.part)

  def __str__(self):
    return self.__unicode__()