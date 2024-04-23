from django.shortcuts import render,HttpResponse
from django.contrib.auth import authenticate,login,logout
from .models import *
import traceback
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import  Response
from django.http import JsonResponse
def home(request):
    return render(request,"index.html")

def signIn(request):
    products=productList.objects.all().values()
    if request.user.is_authenticated and request.user.is_superuser:
        return render(request,"home.html",{"products":products})
    if request.method=="POST":
        usrname=request.POST.get("username")
        password=request.POST.get("password")

        usr = authenticate(request,username=usrname,password=password)
        
        if usr is not None :
            login(request,usr)
            if  request.user.is_superuser:
                return render(request,"home.html",{"products":products})
            else:
                return render(request,"index.html",{"msg":"Username or Password not match or no Permissions"})
        else:
            return render(request,"index.html",{"msg":"Username or Password not match or no Permissions"})
    else:
        return render(request,"index.html",{"msg":"Username or Password not match or no Permissions"})
    
def signOut(request):
    logout(request)
    return render(request,"index.html")
def add_product(request):
    if request.method=="POST":
        product_name=request.POST.get("product_name")
        product_price=request.POST.get("product_price")
        product_description=request.POST.get("product_description")
        product_quantity=request.POST.get("product_quantity")
        print(product_price,"product_price")
        data=productList.objects.create(name=product_name,price=product_price,description=product_description,qty=product_quantity)
        products=productList.objects.all().values()
        return render(request,"home.html",{"products":products})
    return render(request,"add_product.html")
        

def update(request,id):
    if request.method=="POST":
        try:
            product_name=request.POST.get("product_name")
            product_price=request.POST.get("product_price")
            product_description=request.POST.get("product_description")
            product_quantity=request.POST.get("product_quantity")
            data=productList.objects.filter(id=id).update(name=product_name,price=product_price,description=product_description,qty=product_quantity)
            products=productList.objects.all().values()
            return render(request,"home.html",{"products":products})
        except:
            products=productList.objects.all().values()
            return render(request,"home.html",{"products":products})

    products=productList.objects.all().values()
    try:
        data=productList.objects.get(id=id)
        return render(request,"add_product.html",{"data":data})
    except:
        return render(request,"home.html",{"products":products})
    
def delete(request,id):
    try:
        data=productList.objects.filter(id=id).delete()
        print("deleted")
        return HttpResponse("success")
    except:
        return HttpResponse("failed")
    

@csrf_exempt
def get_details(request):
    ids=(request.POST.getlist("ids[]"))
    print(ids)
    total_cost=0
    data=productList.objects.filter(id__in=ids)
    tbody=""
    for item in data:
        total_cost+=int(item.price)
        tbody+=f''' <tr>
                    
                    <td>{item.name}</td>
                    <td>{item.price}</td>
                    <td>{item.description}</td>
                </tr>
        '''
    return JsonResponse(data={"total_cost":total_cost,"tbody":tbody})
    