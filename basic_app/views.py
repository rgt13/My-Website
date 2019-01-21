from django.shortcuts import render
from django.views.generic import (  View,
                                    TemplateView,
                                    ListView,
                                    DetailView,
                                    CreateView,
                                    UpdateView,
                                    DeleteView)
import models

# Create your views here.

def index(request):
    return render(request, "basic_app/index.html")

class IndexView(TemplateView):
    template_name = 'index.html'

def about(request):
    return render(request, "basic_app/aboutpage.html")

def gifgenerator(request):
    return render(request, "basic_app/gifgenerator.html")

def projects(request):
    return render(request, "basic_app/projects.html")

class ProjectListView(ListView):
    context_object_name = "projects"
    model = models.ProjectModel

class ProjectDetailView(DetailView):
    context_object_name = "project_detail"
    model = models.ProjectModel
    template_name = "basic_app/project_detail.html"

def colorgame(request):
    return render(request, "basic_app/Color.html")
