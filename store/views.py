from django.shortcuts import render

def home(request):
    return render(request,"home.html",{})

def index(request):
    return render(request,"index.html",{})


def shopSingle(request):
    return render(request,"shop-single.html",{})

def shop(request):
    return render(request,"shop.html",{})