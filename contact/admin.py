from django.contrib import admin
from contact.models import contactenq

# Register your models here.

class ContactEnqAdmin(admin.ModelAdmin):
    list_display=['name','email','phone','event_type','event_date','subject','message']

admin.site.register(contactenq, ContactEnqAdmin)
