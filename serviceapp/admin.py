from django.contrib import admin
from serviceapp.models import servicedetail, servicedetaill

# Register your models here.


class ServiceDetailAdmin(admin.ModelAdmin):
    list_display=['s_img','s_des','s_title']

admin.site.register(servicedetail, ServiceDetailAdmin)

class ServiceDetaillAdmin(admin.ModelAdmin):
    list_display=['s_imgl','s_desl','s_titlel']

admin.site.register(servicedetaill, ServiceDetaillAdmin)