from django.contrib import admin
from main.models import Manufacturer, Cereal


# Register your models here.

class CerealAdmin(admin.ModelAdmin):
	# list_display = ('name', 'manufacturer', 'cereal_type', 'calories', 'protein', 'fat', 'sodium', 'dietary_fiber', 'carbs', 'sugars', 'display_shelf', 'potassium', 'vit_min', 'serving_size_weight', 'cups_per_serving')
	search_fields = ['name']


admin.site.register(Manufacturer, CerealAdmin)
admin.site.register(Cereal)