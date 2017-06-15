from django.contrib import admin
from Portal.models import Subcategory

class SubcategoryAdmin(admin.ModelAdmin):
  list_display = ('name',
                  'category',
                  'parts_count')
  list_filter = ('category',)

  def parts_count(self, obj):
    return obj.parts.count()

  parts_count.short_description = '# of Parts'

admin.site.register(Subcategory, SubcategoryAdmin)