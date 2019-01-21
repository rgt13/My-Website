from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from basic_app import views

# TEMPLATE TAGGING
app_name = "basic_app"

urlpatterns = [
    path("about/", views.about, name='about'),
    path("gifgenerator/", views.gifgenerator, name='gifgenerator'),
    path("projects/", views.projects, name='projects'),
    path("colorgame/", views.colorgame, name="colorgame"),
    path("project_list", views.ProjectListView.as_view(), name="list")
]
