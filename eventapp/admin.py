from django.contrib import admin
from eventapp.models import programs, latprograms, upcprograms

# Register your models here.
class ProgramAdmin(admin.ModelAdmin):
    list_display=['programs_img','programs_name','programs_detail']

admin.site.register(programs, ProgramAdmin)

class LatProgramAdmin(admin.ModelAdmin):
    list_display=['latprograms_img','latprograms_name','latprograms_detail']

admin.site.register(latprograms, LatProgramAdmin)

class UpcProgramAdmin(admin.ModelAdmin):
    list_display=['upcprograms_img','upcprograms_name','upcprograms_detail']

admin.site.register(upcprograms, UpcProgramAdmin)
