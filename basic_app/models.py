from django.db import models

# Create your models here.
class ImageModel(models.Model):
    name = models.CharField(max_length=255, null=True)
    image = models.ImageField(upload_to="uploads", null=True)
    extension = models.CharField(max_length=255, null=True)


class ProjectModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=500)
    languages = models.ManyToManyField(ImageModel, related_name="images")

    def __str__(self):
        return self.name
