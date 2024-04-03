from django.test import TestCase
from django.urls import reverse
from base.models import *
from django.conf import settings

class ViewsTestCase(TestCase):
    def setUp(self):
        # Create sample data for testing
        self.main_menu = MainMenu.objects.create(name="Main Menu")
        self.textbook_lan = TextbookLanguages.objects.create(name="Urdu")
        self.textbook_category = TextbooksCategories.objects.create(name="Textbook Category", language_associated=self.textbook_lan)
        self.education_category = EducationCategory.objects.create(name="Education Category")
        self.culture_category = CultureCategory.objects.create(name="Culture Category")
        self.footer_detail = FooterDetail.objects.create(
            
            email = "abc@gmail.com",
            phone_number = "12345678901",
            short_description = "Lorem Ipsum.",
        )
        self.important_link = FooterImportantLinks.objects.create(name="Important Link", detail="Lorem Ipsum")

    def test_main_menus(self):
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, self.main_menu.name)

    def test_textBookcategories(self):
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['textBookcategories'].first(), self.textbook_category)

    def test_educationCategories(self):
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['educationCategories'].first(), self.education_category)


    def test_cultureCategories(self):
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['cultureCategories'].first(), self.culture_category)

    def test_footerdetails(self):
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['footerdetails'], self.footer_detail)


    def test_homepage_url(self):
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['homepage_url'], settings.OSCAR_HOMEPAGE)

    def test_important_links(self):
        response = self.client.get(reverse('homepage'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context['important_links'].first(), self.important_link)
