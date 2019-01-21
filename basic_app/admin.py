from django.contrib import admin
from basic_app.models import ProjectModel, ImageModel, WorkModel, LogoModel

# Register your models here.
admin.site.register(ProjectModel)
admin.site.register(ImageModel)
admin.site.register(WorkModel)
admin.site.register(LogoModel)
