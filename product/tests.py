from django.test import TestCase
from users.models import User
from .models import Category, Product
from decimal import Decimal

class CategoryProductModelTest(TestCase):
    def setUp(self):
        # Foydalanuvchi yaratamiz
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123'
        )

        # Kategoriya yaratamiz
        self.category = Category.objects.create(name="Elektronika")

        # Mahsulot yaratamiz
        self.product = Product.objects.create(
            name="Smartfon",
            user=self.user,
            price=Decimal('199.99'),
            category=self.category,
            description="Yangi model smartfon"
        )

    def test_category_str(self):
        """Category modelining __str__ metodi to'g'ri ishlayaptimi"""
        self.assertEqual(str(self.category), "Elektronika")

    def test_product_str(self):
        """Product modelining __str__ metodi to'g'ri ishlayaptimi"""
        self.assertEqual(str(self.product), "Smartfon")

    def test_product_fields(self):
        """Product maydonlari to'g'ri saqlanyaptimi"""
        self.assertEqual(self.product.name, "Smartfon")
        self.assertEqual(self.product.user.username, "testuser")
        self.assertEqual(self.product.price, Decimal('199.99'))
        self.assertEqual(self.product.category.name, "Elektronika")
        self.assertEqual(self.product.description, "Yangi model smartfon")

    def test_category_relation(self):
        """Category -> Products munosabat to'g'riligi"""
        self.assertIn(self.product, self.category.products.all())
