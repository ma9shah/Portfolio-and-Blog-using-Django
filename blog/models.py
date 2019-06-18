from django.db import models
import datetime
# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=50)
    content=models.CharField(max_length=100)
    # date=models.DateTimeField(default=datetime.date.today)
    image=models.ImageField(upload_to='blog_photos')
    # created_at = models.DateTimeField('_Date',auto_now_add=True)
