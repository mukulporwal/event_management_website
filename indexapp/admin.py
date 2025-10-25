from django.contrib import admin
from indexapp.models import event, gallery


# Register your models here.
class EventAdmin(admin.ModelAdmin):
    list_display=['event_img','event_name']
 
admin.site.register(event, EventAdmin)

class GalleryAdmin(admin.ModelAdmin):
    list_display=['gallery_img']

admin.site.register(gallery, GalleryAdmin)