from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,"index.html")

def about(request):
    return render(request,"about.html")

def tech(request):
    return render(request,"technical.html")
def sol(request):
    return render(request,"solution.html")
def innov(request):
    return render(request,"innovation.html")
def impact(request):
    return render(request,"impact.html")