from django.contrib import admin
from Portal.models import Listing

class ListingAdmin(admin.ModelAdmin):
  list_display = ('code',
                  'title',
                  'status',
                  'added_on')
  list_filter = ('status',
                 'part__brand',
                 'added_on')
  search_fields = ('code',
                   'title',
                   'part__name',
                   'part__brand__name')
  fields = ('added_on',
            'last_modified_on',
            'code',
            'status',
            'part',
            'title',
            'subtitle',
            'description',
            'price',
            'condition',
            'location',
            'contact_info',
            'email',
            'photo_1',
            'photo_2',
            'photo_3',
            'photo_4')

  readonly_fields = ('added_on', 'last_modified_on')

  # todo: add part column
  # def get_part(self, obj):
  #   return str(obj.part)

  # get_part.short_description = 'Part'
  # get_part.admin_order_field = ['part__brand__name', 'part__name']

admin.site.register(Listing, ListingAdmin)