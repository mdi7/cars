from django.contrib import admin
from .models import CarsModel
from django.utils.html import format_html
# Register your models here.

class PhotoAdmin(admin.ModelAdmin):


    def img_rep(self):
        return format_html("<img src='/{}' style='height:50px; width:auto;'>", self.image)
    list_display=('make','model_num',img_rep)
    search_fields = ('make','model_num')
admin.site.register(CarsModel,PhotoAdmin)
