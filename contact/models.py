from django.db import models

# Create your models here.
class contactenq(models.Model):
    name=models.CharField(max_length=60)
    email=models.CharField(max_length=60)
    phone=models.CharField(max_length=60)
    event_type=models.CharField(max_length=60)
    event_date=models.DateField()
    subject=models.CharField(max_length=60)
    message=models.TextField()