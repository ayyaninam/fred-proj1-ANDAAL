from django.test import TestCase
from base.models import *

from django.contrib.auth import get_user_model
User = get_user_model()

class UserModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        User.objects.create(username='testuser', email='test@example.com', first_name='Test')

    def test_username_label(self):
        user = User.objects.get(id=1)
        field_label = user._meta.get_field('username').verbose_name
        self.assertEqual(field_label, 'username')

    def test_username_max_length(self):
        user = User.objects.get(id=1)
        max_length = user._meta.get_field('username').max_length
        self.assertEqual(max_length, 1000)

    def test_phone_number_blank(self):
        user = User.objects.get(id=1)
        self.assertTrue(user.phone_number == '')

    def test_str_representation_with_email(self):
        user = User.objects.get(id=1)
        expected_str = 'test@example.com'
        self.assertEqual(str(user), expected_str)

    def test_str_representation_without_email(self):
        user = User.objects.get(id=1)
        user.email = ''
        expected_str = 'Test'
        self.assertEqual(str(user), expected_str)

    # Add more tests for other fields and constraints as needed
        

class FooterImportantLinksModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        FooterImportantLinks.objects.create(name='Link 1', detail='Detail for Link 1')

    def test_name_label(self):
        link = FooterImportantLinks.objects.get(id=1)
        field_label = link._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    def test_detail_label(self):
        link = FooterImportantLinks.objects.get(id=1)
        field_label = link._meta.get_field('detail').verbose_name
        self.assertEqual(field_label, 'detail')

    def test_name_max_length(self):
        link = FooterImportantLinks.objects.get(id=1)
        max_length = link._meta.get_field('name').max_length
        self.assertEqual(max_length, 255)

    # Add more tests for other fields and constraints as needed

    def test_str_representation(self):
        link = FooterImportantLinks.objects.get(id=1)
        expected_str = 'Link 1'
        self.assertEqual(str(link), expected_str)

    # Add more tests as needed
