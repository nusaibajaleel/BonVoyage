from django.shortcuts import render
from . models import Place,Destination

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    return render(request,"index.html",{'result':obj})
def dest(request):
    obj=Destination.objects.all()
    return render(request,"index.html",{'res':obj})