from django.contrib import admin
from .models import Cars

# Register your models here.

class CarsAdmin (admin.ModelAdmin):
    list_display=('reg_no','location','model')
    list_display_links =('reg_no',)
    search_fields =('reg_no','locality','model')

admin.site.register(Cars,CarsAdmin)
