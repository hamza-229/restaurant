from django.test import TestCase
from .models import *
from .views import *
from .serializers import *
from rest_framework import response, status
from django.urls import reverse

class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(Title="IceCream", Price=22.23, Inventory=100)
        Menu.objects.create(Title="Chocolate", Price=10.5, Inventory=50)

    def test_getall(self):
        response = self.client.get(reverse('menu-items'), format='json')
        
        self.assertEqual(response.status_code, 200)
       