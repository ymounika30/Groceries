from django.shortcuts import render
from . models import *

def home(request):
    items=Items.objects.all()
    context={'items':items}
    return render(request,'home.html',context)

def store(request):
    items=Items.objects.all()
    item_count=items.count()
    context={'items':items,'item_count':item_count}
    return render(request,'store.html',context)