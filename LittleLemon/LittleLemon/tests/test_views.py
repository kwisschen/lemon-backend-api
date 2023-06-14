from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User

from LittleLemonAPI.models import MenuItem
from LittleLemonAPI.serializers import MenuItemSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        user = User.objects.create_user(username="testuser", password="testpass")
        self.token = Token.objects.create(user=user)
        self.client.force_authenticate(user=user)
        MenuItem.objects.create(title="Dish1", price=15, inventory=500)
        MenuItem.objects.create(title="Dish2", price=25, inventory=50)
        MenuItem.objects.create(title="Dish3", price=150, inventory=5)

    def test_getall(self):
        response = self.client.get("/api/menu-items/")
        items = MenuItem.objects.all()
        serializer = MenuItemSerializer(items, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_getone(self):
        item = MenuItem.objects.create(title="DishA", price=50, inventory=25)
        response = self.client.get(f"/api/menu-items/{item.id}/")
        serializer = MenuItemSerializer(item)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)
