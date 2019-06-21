from django.shortcuts import render
from .models import Job
# Create your views here.
def home(req):
    joblist=Job.objects.all
    return render(req, 'home.html',{'joblist': joblist})
def contact(req):
    return render(req, 'form.html')