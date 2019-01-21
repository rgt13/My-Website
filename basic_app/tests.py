from django.test import TestCase
from basic_app import views
from basic_app import models
# Create your tests here.
class MethodTest(TestCase):

    def test_createIndex(self):
        index = views.index
        assert index != None

    def test_createAboutPage(self):
        about = views.about
        assert about != None

    def test_createImageModel(self):
        image = models.ImageModel("fsu", "png")
        assert image.file == "fsu.png"

    def test_createImageJson(self):
        image = models.ImageModel("fsu", "png")
        self.assertEquals(image.json(), {
            'name': 'fsu',
            'extension': 'png'
        })

    def test_createProjectModel(self):
        image1 = models.ImageModel("csharp", "png").json()
        image2 = models.ImageModel("unity", "png").json()
        project = models.ProjectModel("Project", "Project Description")
        assert project.name == "Project"
        assert project.description == "Project Description"


    def test_createProjectJson(self):
        project = models.ProjectModel("Project", "Project Description")
        self.assertEquals(project.json(), {
            'name': 'Project',
            'description': 'Project Description'
        })

    def test_createLogoModel(self):
        logo = models.LogoModel("fsu", "png")
        assert logo.file == "fsu.png"

    def test_createLogoJson(self):
        logo = models.LogoModel("fsu", "png")
        self.assertEquals(logo.json(), {
            'name': 'fsu',
            'extension': 'png'
        })

    def test_createWorkModel(self):
        work = models.WorkModel("Software Developer", "Company", "I did stuff")
        assert work.position == "Software Developer"
        assert work.company == "Company"
        assert work.description == "I did stuff"

    def test_createWorkJson(self):
        work = models.WorkModel("Position", "Company", "Things")
        self.assertEquals(work.json(), {
            'position': 'Position',
            'company': 'Company',
            'description': 'Things'
        })
