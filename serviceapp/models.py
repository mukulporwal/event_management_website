from django.db import models

# Create your models here.

    
class servicedetail(models.Model):
    s_title=models.CharField(max_length=60 , null=True)
    s_img=models.CharField(max_length=60)
    s_des=models.CharField(max_length=200)

class servicedetaill(models.Model):
    s_titlel=models.CharField(max_length=60 , null=True)
    s_imgl=models.CharField(max_length=60)
    s_desl=models.CharField(max_length=200)
