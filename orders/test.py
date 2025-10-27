from django.test import TestCase
from decimal import Decimal
from django.contrib.auth.models import User
from home.models import MenuItem
from orders.models import Order , OrderItem

class OrderTotalCalculationTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username = 'kr', password='jaybharat')

        self.item1 = MenuItem.objects.create(name='pizza',price=Decimal('250.00'))
        self.item2 = MenuItem.objects.create(name ='Burger', price=Decimal('150.00'))

        self.order = Order.objects.create(user=self.user,order_id='ORD1001')

        OrderItem.objects.create(order=self.order , menu_item=self.item1 , quantity=2, price=self.item1.price)
        OrderItem.objects.create(order=self.order , menu_item=self.item2 , quantity=1, price=self.item2.price)

    def test_calculate_total(self):
        total = self.order.calculate_total()
        self.assertEqual(total,Decimal('650.00'))
            