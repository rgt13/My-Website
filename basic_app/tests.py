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
        pass
