from django.shortcuts import render
from . models import *

def home(request):
    items=Items.objects.all()
    context={'items':items}
    return render(request,'home.html',context)

