from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "basic_app/index.html")

def about(request):
    return render(request, "basic_app/aboutpage.html")

def gifgenerator(request):
    return render(request, "basic_app/gifgenerator.html")

def projects(request):
    return render(request, "basic_app/projects.html")

def colorgame(request):
    return render(request, "basic_app/Color_Game/Color.html")
