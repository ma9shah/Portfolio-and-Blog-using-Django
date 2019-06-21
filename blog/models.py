from django.db import models
from datetime import datetime
# Create your models here.
class Blog(models.Model):
    title=models.CharField(max_length=50)
    content=models.TextField()
    blog_date=models.DateTimeField(default=datetime.now)
    image=models.ImageField(upload_to='blog_photos')

    def __str__(self):
        return self.title
    def summary(self):
        split=self.content.split()
        i=0
        summary=''
        for i in range(0,40):
            summary+=split[i]+' '
        summary+='...'
        return summary    