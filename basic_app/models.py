from django.db import models

# Create your models here.
class LogoModel(models.Model):
    name = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to="uploads", null=True)
    extension = models.CharField(max_length=255, null=True)
    # file = str(str(name) + "." + str(extension))



class ImageModel(models.Model):
    name = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to="uploads", null=True)
    extension = models.CharField(max_length=255, null=True)
    # file = str(str(name) + "." + str(extension))



class ProjectModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    languages = models.ManyToManyField(ImageModel, related_name="images")



class WorkModel(models.Model):
    position = models.CharField(max_length=255, null=True)
    company = models.CharField(max_length=255, null=True)
    logo = models.ManyToManyField(LogoModel, related_name="logos")
    description = models.CharField(max_length=1000, null=True)
