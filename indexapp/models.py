from django.db import models

# Create your models here.

class event(models.Model):
    event_img=models.CharField(max_length=50)
    event_name=models.CharField(max_length=50 , null=True)

class gallery(models.Model):
    gallery_img=models.CharField(max_length=50, null=True)

