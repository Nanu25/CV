from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "cvsite/index.html")

def about(request):
    return render(request, "cvsite/about.html")

def portfolio(request):
    return render(request, "cvsite/portfolio.html")

def contact(request):
    return render(request, "cvsite/contact.html")