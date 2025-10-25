from django.contrib import admin
from galleryapp.models import gallimg, gallimg1

# Register your models here.
class GallImgAdmin(admin.ModelAdmin):
    list_display=['g_img']

admin.site.register(gallimg, GallImgAdmin)

class GallImg1Admin(admin.ModelAdmin):
    list_display=['g_img1']

admin.site.register(gallimg1, GallImg1Admin)