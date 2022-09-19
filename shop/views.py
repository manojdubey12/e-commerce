from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request,"shop/index.html")

def about(request):
    return HttpResponse("shop about")

def contact(request):
    return HttpResponse("shop contact")

def trackers(request):
    return HttpResponse("shop trackers")

def search(request):
    return HttpResponse("shop search")

def productView(request):
    return HttpResponse("shop productView")
