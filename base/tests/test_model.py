from django.test import TestCase
from base.models import *
from apps.catalogue.models import Category as Oscar_Category
import datetime

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
        self.assertTrue(user.phone_number == None)

    def test_str_representation_with_email(self):
        user = User.objects.get(id=1)
        expected_str = 'test@example.com'
        self.assertEqual(str(user), expected_str)

    def test_str_representation_without_email(self):
        user = User.objects.get(id=1)
        user.email = ''
        expected_str = 'Test'
        self.assertEqual(str(user), expected_str)


class MainMenuTestCase(TestCase):
    def test_main_menu_creation(self):
        main_menu_full = MainMenu.objects.create(
            name="Test Menu",
            icons_link="test_icon",
            redirect_to_link="/test",
            category_attached=None
        )
        self.assertIsNotNone(main_menu_full.id)
        self.assertEqual(str(main_menu_full), "Test Menu")

        main_menu_category = MainMenu.objects.create(
            name="Category Menu",
            icons_link="category_icon",
            redirect_to_link="/category",
        )
        self.assertIsNotNone(main_menu_category.id)
        self.assertEqual(str(main_menu_category), "Category Menu")

        main_menu_minimal = MainMenu.objects.create(
            name="Minimal Menu",
            icons_link=None,
            redirect_to_link=None,
            category_attached=None
        )
        self.assertIsNotNone(main_menu_minimal.id)
        self.assertEqual(str(main_menu_minimal), "Minimal Menu")


class TextbookModelsTestCase(TestCase):
    def setUp(self):
        self.language = TextbookLanguages.objects.create(name="English")
        self.category = TextbooksCategories.objects.create(name="Mathematics", language_associated=self.language)
        self.oscar_category = Oscar_Category.objects.create(name='test', depth=1)
        self.class_ = TextbookClasses.objects.create(name="Class 10", products_category=self.oscar_category)

    def test_textbook_language_creation(self):
        language = TextbookLanguages.objects.create(name="French")
        self.assertIsNotNone(language.id)
        self.assertEqual(str(language), "French")

    def test_textbook_classes_creation(self):
        class_ = TextbookClasses.objects.create(name="Class 11", products_category=self.oscar_category)
        self.assertIsNotNone(class_.id)
        self.assertEqual(str(class_), "Class 11")

    def test_textbooks_categories_creation(self):
        category = TextbooksCategories.objects.create(name="Science", language_associated=self.language)
        category.child_classes.add(self.class_)
        self.assertIsNotNone(category.id)
        self.assertEqual(str(category), "Science")



class EducationModelsTestCase(TestCase):
    def setUp(self):
        self.category = EducationCategory.objects.create(name="Math", default=False)

    def test_education_category_creation(self):
        category = EducationCategory.objects.create(name="Science", default=True)
        self.assertIsNotNone(category.id)
        self.assertEqual(str(category), "Science")

    def test_education_creation(self):
        # Test creating an Education instance
        education = Education.objects.create(
            owner_or_institution_name="Test Institute",
            title="Test Education",
            short_description="Short description",
            description="Long description",
            location="Test Location",
            link_to_orignal="https://example.com",
        )
        education.category.add(self.category)
        self.assertIsNotNone(education.id)
        self.assertEqual(str(education), "Test Education")




class CultureModelsTestCase(TestCase):
    def setUp(self):
        self.category = CultureCategory.objects.create(name="Art", default=False)

    def test_culture_category_creation(self):
        category = CultureCategory.objects.create(name="Music", default=True)
        self.assertIsNotNone(category.id)
        self.assertEqual(str(category), "Music")

    def test_culture_creation(self):
        culture = Culture.objects.create(
            owner_or_institution_name="Test Institute",
            title="Test Culture",
            short_description="Short description",
            description="Long description",
            date="2024-04-03",
            location="Test Location",
            link_to_orignal="https://example.com",
            recommended=True
        )
        culture.category.add(self.category)
        self.assertIsNotNone(culture.id)
        self.assertEqual(str(culture), "Test Culture")




class ShippingMethodTestCase(TestCase):
    def setUp(self):
        self.shipping_method = ShippingMethod.objects.create(
            name="Standard Shipping",
            code="STD",
            charge_excl_tax=100,
            charge_incl_tax=120
        )

    def test_shipping_method_creation(self):
        shipping_method = ShippingMethod.objects.create(
            name="Express Shipping",
            code="EXP",
            charge_excl_tax=200,
            charge_incl_tax=240
        )
        shipping_method.countries.add(AddressCountry.objects.create(name="USA"))
        self.assertIsNotNone(shipping_method.id)
        self.assertEqual(str(shipping_method), "Express Shipping")

    def test_clean_method(self):
        shipping_method = ShippingMethod.objects.create(
            name="International Shipping",
            code="INT",
            charge_excl_tax=150,
            charge_incl_tax=180
        )
        shipping_method.countries.add(AddressCountry.objects.create(name="UK"))
        shipping_method.clean()
        self.assertIsNone(shipping_method.code)
        self.assertIsNone(shipping_method.charge_excl_tax)
        self.assertIsNone(shipping_method.charge_incl_tax)
        self.assertEqual(shipping_method.countries.count(), 0)





class XafTesting(TestCase):
    def setUp(self):
        self.rate = RateOfEuro.objects.create(base="EUR", date=datetime.date(2024, 4, 3), xaf_to_euro=655.43)


    def test_rate_of_euro_creation(self):
        rate = RateOfEuro.objects.create(base="EUR", date=datetime.date(2024, 4, 4), xaf_to_euro=665.43)
        self.assertIsNotNone(rate.id)
        self.assertEqual(rate.base, "EUR")
        self.assertEqual(rate.date, datetime.date(2024, 4, 4))
        self.assertEqual(rate.xaf_to_euro, 665.43)
        self.assertEqual(str(rate), "XAF TO EURO is: 665.43")


class FooterTest(TestCase):

    def setup(self):
        self.footer_detail = FooterDetail.objects.create(email="test@example.com", phone_number="1234567890", short_description="Test Description")

    def test_footer_detail_creation(self):
        # Test creating a FooterDetail instance
        footer_detail = FooterDetail.objects.create(email="example@example.com", phone_number="9876543210", short_description="Another Description")
        self.assertIsNotNone(footer_detail.id)
        self.assertEqual(footer_detail.email, "example@example.com")
        self.assertEqual(footer_detail.phone_number, "9876543210")
        self.assertEqual(footer_detail.short_description, "Another Description")
        self.assertEqual(str(footer_detail), "example@example.com - 9876543210")




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

    def test_str_representation(self):
        link = FooterImportantLinks.objects.get(id=1)
        expected_str = 'Link 1'
        self.assertEqual(str(link), expected_str)
