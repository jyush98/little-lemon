# tests/test_views.py

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from restaurant.models import MenuItem
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):

    def setUp(self):
        """
        Setup method that will create a few MenuItem instances for testing.
        """
        self.client = APIClient()  # Initialize the test client
        self.menu_item_1 = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
        self.menu_item_2 = MenuItem.objects.create(title="Pizza", price=120, inventory=50)
        self.url = "/restaurant/menu/"  # Adjust to your actual endpoint URL
    def test_get_all_menu_items(self):
        """
        Test that the view returns all menu items serialized correctly.
        """
        response = self.client.get(self.url)  # Send a GET request to the API endpoint
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        expected_data = MenuSerializer([self.menu_item_1, self.menu_item_2], many=True).data
        self.assertEqual(response.data, expected_data)
