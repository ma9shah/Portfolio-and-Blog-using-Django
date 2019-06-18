from django.db import models
from datetime import datetime
# Create your models here.
class Job(models.Model):
        image=models.ImageField(upload_to='job_photos/')
        description=models.CharField(max_length=250, default="")
        photo_date = models.DateTimeField(default=datetime.now)
        