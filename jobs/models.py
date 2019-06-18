from django.db import models

# Create your models here.
class Job(models.Model):
        image=models.ImageField(upload_to='job_photos/')
        description=models.CharField(max_length=250)
        