from django.test import TestCase
from .models import Category, Image, Location

# Create your tests here.

class CategryTestCase(TestCase):
    # setup method
    def setUp(self):
        self.img = Category(name = 'img')
# Testing instance
    def test_instance(self):
        self.assertTrue(isinstance(self.img,Category))
