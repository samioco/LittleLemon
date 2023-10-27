from django.test import TestCase
from restaurant.models import MenuItem

class MenuItemTest(TestCase):
  def test_get_menu_item(self):
    item = MenuItem.objects.create(title="IceCream", price=80, inventory=100)
    # itemstr = item.get_item()
    
    self.assertEqual(item, "IceCream : 80")