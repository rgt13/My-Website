from django.db import models

# Create your models here.
class LogoModel(models.Model):
    name = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to="uploads", null=True)
    extension = models.CharField(max_length=255, null=True)
    file = str(str(name) + "." + str(extension))

    def __init__(self, name, extension):
        self.name = str(name)
        self.extension = str(extension)
        self.file = str(name + "." + extension)

    def json(self):
        return {
            'name': self.name,
            'extension': self.extension
        }

    def __str__(self):
        return self.name

class ImageModel(models.Model):
    name = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to="uploads", null=True)
    extension = models.CharField(max_length=255, null=True)
    file = str(str(name) + "." + str(extension))

    def __init__(self, name, extension):
        self.name = str(name)
        self.extension = str(extension)
        self.file = str(name + "." + extension)

    def json(self):
        return {
            'name': self.name,
            'extension': self.extension
        }

    def __str__(self):
        return "Image: {}.{}".format(name, extension)

class ProjectModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    languages = models.ManyToManyField(ImageModel, related_name="images")

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def json(self):
        return {
            'name': self.name,
            'description': self.description
        }

    def __str__(self):
        return self.name

class WorkModel(models.Model):
    position = models.CharField(max_length=255, null=True)
    company = models.CharField(max_length=255, null=True)
    logo = models.ManyToManyField(LogoModel, related_name="logos")
    description = models.CharField(max_length=1000, null=True)

    def __init__(self, position, company, description):
        self.position = position
        self.company = company
        self.description = description

    def json(self):
        return {
            'position': self.position,
            'company': self.company,
            'description': self.description
        }
