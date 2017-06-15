from django.contrib import admin
from Portal.models import Category, Subcategory

class SubcategoryInline(admin.TabularInline):
  model = Subcategory
  extra = 0

class CategoryAdmin(admin.ModelAdmin):
  inlines = [SubcategoryInline,]
  list_display = ('name',
                  'subcategories_count')

  def subcategories_count(self, obj):
    return obj.subcategories.count()

  subcategories_count.short_description = '# of Subcategories'

admin.site.register(Category, CategoryAdmin)