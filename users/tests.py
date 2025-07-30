from django.test import TestCase
from .models import User, CUSTOMER, EMPLOYEE, ADMIN


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass123',
            phone_number='+998901234567',
            bio='Test bio',
            user_roles=EMPLOYEE,
            email='test@example.com'
        )

    def test_user_str(self):
        """User modelining __str__ metodi username ni qaytaryaptimi"""
        self.assertEqual(str(self.user), 'testuser')

    def test_user_fields(self):
        """User modelining maydonlari to‘g‘ri ishlayaptimi"""
        self.assertEqual(self.user.phone_number, '+998901234567')
        self.assertEqual(self.user.bio, 'Test bio')
        self.assertEqual(self.user.user_roles, EMPLOYEE)
        self.assertEqual(self.user.email, 'test@example.com')
        self.assertTrue(self.user.check_password('testpass123'))

    def test_user_role_choices(self):
        """User role qiymatlari belgilangan variantlardan biriga tengmi"""
        self.assertIn(self.user.user_roles, [CUSTOMER, EMPLOYEE, ADMIN])

    def test_user_base_model_fields(self):
        """BaseModel'dan meros olingan created_at va updated_at ishlayaptimi"""
        self.assertIsNotNone(self.user.created_at)
        self.assertIsNotNone(self.user.updated_at)
