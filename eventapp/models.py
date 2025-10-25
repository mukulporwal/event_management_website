from django.db import models

# Create your models here.
class programs(models.Model):
    programs_img=models.CharField(max_length=100)
    programs_name=models.CharField(max_length=100)
    programs_detail=models.CharField(max_length=100)

class latprograms(models.Model):
    latprograms_img=models.CharField(max_length=100)
    latprograms_name=models.CharField(max_length=100)
    latprograms_detail=models.CharField(max_length=100)

class upcprograms(models.Model):
    upcprograms_img=models.CharField(max_length=100)
    upcprograms_name=models.CharField(max_length=100)
    upcprograms_detail=models.CharField(max_length=100)