from django.shortcuts import render
from django.http import HttpResponse

from .models import Product
from math import ceil, prod

# def index(request):
#     allProds= []
#     # allprods= [[products, range(1, nslides), nslides],[products, range(1, nslides), nslides]]
#     # print(allprods)
#     # params = {"allprods": allprods}
#     catprods = Product.objects.values('category', 'id')
#     cats={item['category'] for item in catprods}
#     for cat in cats:
#         prod= Product.objects.filter(category=cat)
#         n= len(prod)
#         nSlides = n//4 + ceil((n/4) - (n//4))
#         allProds.append([prod,range(1, nSlides),nSlides])

#     params = {"allProds": allProds}
#     #params ={'nslides': nslides, 'range': range(1, nslides), 'products': products}
#     return render(request,"shop/index.html",params)

def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))

    allProds = []
    catprods = Product.objects.values('category', 'id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    params = {'allProds':allProds}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request,"shop/about.html")

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone= request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        print(name, email, phone, desc)
    return render(request,"shop/contact.html")

def trackers(request):
    return render(request,"shop/tracker.html")

def search(request):
    return render(request,"shop/search.html")

def productView(request,myid):
    product= Product.objects.get(id=myid)
    return render(request, 'shop/prodView.html',{'product':product})

def checkout(request):
    return render(request, 'shop/checkout.html')
