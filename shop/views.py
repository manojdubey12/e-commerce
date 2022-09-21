from django.shortcuts import render
from django.http import HttpResponse

from .models import Product
from math import ceil

def index(request):
    products= Product.objects.all()
    allprods= []
    # allprods= [[products, range(1, nslides), nslides],[products, range(1, nslides), nslides]]
    # print(allprods)
    # params = {"allprods": allprods}
    catprods = Product.objects.values('category', 'id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod= Product.objects.filter(category=cat)
        n= len(products)
        nslides = n//4 + ceil((n/4) + (n//4))
        allprods.append([prod,range(1, nslides),nslides])

    params = {"allprods": allprods}
    #params ={'nslides': nslides, 'range': range(1, nslides), 'products': products}
    return render(request,"shop/index.html",params)

def about(request):
    return render(request,"shop/about.html")

def contact(request):
    return HttpResponse("shop contact")

def trackers(request):
    return HttpResponse("shop trackers")

def search(request):
    return HttpResponse("shop search")

def productView(request):
    return HttpResponse("shop productView")
