from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse
from .models import *
from project import settings

# Create your views here.
def index(request):
    return render(request, "index.html")

def test_image(request, pk):
    item = Item.objects.get(pk=pk)
    print(item)
    # print(item.img.url)
    return render(request, "test.html", {"item": item})