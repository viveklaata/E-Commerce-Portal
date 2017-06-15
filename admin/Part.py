from django.contrib import admin
from Portal.models import Part

class PartAdmin(admin.ModelAdmin):
  list_display = ('name',
                  'brand',
                  'subcategory',
                  'listings_count')
  list_filter = ('brand',
                 'subcategory',)
  search_fields = ('name',
                   'brand__name')
  fields = ('subcategory',
            'brand',
            'name')

  def listings_count(self, obj):
    return obj.listings.count()

  listings_count.short_description = '# of Listings'

admin.site.register(Part, PartAdmin)