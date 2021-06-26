from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.urls import reverse
from .models import *
from project import settings
import random, string

def generate_code():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for i in range(7))

####### VIEWS ################################################
def index(request):
    return render(request, "index.html")

def create(request):
    if request.method == "GET":
        items = Item.objects.all()
        return render(request, "create.html", {
            "items": items
        })
    elif request.method == 'POST':
        code = generate_code()
        names = request.POST['array'].split(',')
        print(names)
        items = [Item.objects.get(name=name) for name in names]
        new_course = Course(code=code)
        new_course.save()
        for i, item in enumerate(items):
            new_course.items.add(item, through_defaults={'index': i})
        data = dict(request.POST)
        data.update({"code": code})
        return render(request, "create.html", data)

def explore(request):
    random_id = random.randint(2, Item.objects.count())
    item = Item.objects.get(id=random_id)
    print(item)
    return render(request, "explore.html", {
        "item":item
    })

def course(request, code, index=0):
    course = Course.objects.get(code=code)
    try:
        sequence = Sequence.objects.get(course=course, index=index)
        index+=1
        print(sequence.item)
        return render(request, "course.html", {
            "item":sequence.item, "code":code, "next_index":index
            })
    except:
        return HttpResponseRedirect(reverse('index'))










####### TESTING ################################################
def test_image(request, pk): # TESTING SINGLE IMGS
    item = Item.objects.get(pk=pk)
    print(item)
    # print(item.img.url)
    return render(request, "test.html", {"item": item})

def test_all_img(request): # TESTING ALL IMGS
    items = Item.objects.all()
    return render(request, "test_all_img.html", {
        "items": items
    })
