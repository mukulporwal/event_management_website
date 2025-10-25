from django.contrib import admin
from aboutapp.models import member

# Register your models here.
class MemberAdmin(admin.ModelAdmin):
    list_display=['member_img','member_name','member_work','member_exp']

admin.site.register(member,MemberAdmin)