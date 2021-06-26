from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse
from .models import *
from project import settings

####### VIEWS ################################################
def index(request):
    return render(request, "index.html")


def create(request):
    return render(request, "create.html")











####### TESTING ################################################
def test_image(request, pk): # TESTING SINGLE IMGS
    item = Item.objects.get(pk=pk)
    print(item)
    # print(item.img.url)
    return render(request, "test.html", {"item": item})

def test_all_img(request): # TESTING ALL IMGS
    items = Item.objects.all()
    for i in items:
        print(i)
    return render(request, "test_all_img.html", {
        "items": items
    })
