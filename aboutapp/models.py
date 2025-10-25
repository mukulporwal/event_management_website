from django.db import models

# Create your models here.
class member(models.Model):
    member_img=models.CharField(max_length=100)
    member_name=models.CharField(max_length=100)
    member_work=models.CharField(max_length=100)
    member_exp=models.CharField(max_length=100)