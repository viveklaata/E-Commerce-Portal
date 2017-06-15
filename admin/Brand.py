from django.contrib import admin
from Portal.models import Brand

class BrandAdmin(admin.ModelAdmin):
  list_display = ('name',
                  'parts_count')
  search_fields = ('name',)
  fields = ('name',)

  def parts_count(self, obj):
    return obj.parts.count()

  parts_count.short_description = '# of Parts'

admin.site.register(Brand, BrandAdmin)