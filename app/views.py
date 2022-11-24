from django.shortcuts import render,get_object_or_404
from . models import *

def home(request):
    items=Items.objects.all()
    context={'items':items}
    return render(request,'home.html',context)

def store(request,category_slug=None):
    categories=None
    items=None
    if category_slug != None:
        categories=get_object_or_404(Category,slug=category_slug)
        items=Items.objects.filter(category=categories,is_available=True)
        item_count=items.count()
    else:
        items=Items.objects.all()
        item_count=items.count()
    context={'items':items,'item_count':item_count}
    return render(request,'store.html',context)