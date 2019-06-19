from django.db import models
from datetime import datetime
# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField(max_length=100)
    blog_date=models.DateTimeField(default=datetime.now)
    image=models.ImageField(upload_to='blog_photos')

    def __str__(self):
        return self.title