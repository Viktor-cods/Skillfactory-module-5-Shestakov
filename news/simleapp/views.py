from django.shortcuts import render
from .models import *

def index(request):
    stat= Statia.objects.all()
    return render(request,'index.html',context={'stat':stat})

def detail(request,slug):
    simpl=Statia.objects.get(slug__iexact=slug)
    return render(request,'detail.html',context={'stat':simpl})