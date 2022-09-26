from django.shortcuts import render
from django.http import HttpResponse

from .models import OrderUpdate, Product, Orders
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
    if request.method == "POST":
        items_json= request.POST.get('item_json',"")
        name= request.POST.get('name',"")
        email=request.POST.get('email',"")
        address=request.POST.get('address1',"") + request.POST.get('address2',"")
        city= request.POST.get('city',"")
        state = request.POST.get('state', '')
        zip_code = request.POST.get('zip_code', '')
        phone = request.POST.get('phone', '')
        order = Orders(items_json=items_json, name=name, email=email, address=address, city=city,
                       state=state, zip_code=zip_code, phone=phone)
        order.save()
        update= OrderUpdate(order_id=order.order_id, update_desc= "your order has been placed")
        update.save()
        id = order.order_id
        thank= True
        return render(request, 'shop/checkout.html', {'thank':thank, 'id': id})

    return render(request, 'shop/checkout.html')
