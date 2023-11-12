from django.shortcuts import render
from . models import Places,Team

# Create your views here.

def demo(request):
    place = Places.objects.all()
    team = Team.objects.all()
    return  render(request,"index.html",{'result':place,'team':team})