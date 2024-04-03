from django.test import TestCase, RequestFactory
from django.urls import reverse
from base.models import FooterImportantLinks
from django.test import Client
from base.views import * 
from unittest.mock import patch, MagicMock

from django.contrib.auth import get_user_model
User = get_user_model()

class HomepageViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.menu1 = MainMenu.objects.create(name="Menu 1")
        self.menu2 = MainMenu.objects.create(name="Menu 2")

    def test_homepage_view(self):
        response = self.client.get(reverse('homepage'))

        self.assertEqual(response.status_code, 200)

        self.assertIn('main_menus_wc', response.context)


        main_menus_wc = response.context['main_menus_wc']

        for main_menu, class_name in main_menus_wc:
            self.assertIsInstance(main_menu, MainMenu)
            self.assertIsInstance(class_name, str)



class TextbookLanguageSectionViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # Create some sample TextbookLanguages objects
        self.language1 = TextbookLanguages.objects.create(name="English")
        self.language2 = TextbookLanguages.objects.create(name="French")

    def test_textbook_language_section_view(self):
        # Call the view function using the test client
        response = self.client.get(reverse('textbook_language_section'))

        # Check if the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Check if the all_languages is present in the context
        self.assertIn('all_languages', response.context)

        # Check if the number of all_languages matches the number of TextbookLanguages objects
        all_languages = response.context['all_languages']
        self.assertEqual(all_languages.count(), TextbookLanguages.objects.count())

        # Check if the all_languages queryset contains the expected objects
        self.assertIn(self.language1, all_languages)
        self.assertIn(self.language2, all_languages)


class ClassCategoriesViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # Create a TextbookLanguages object
        self.language = TextbookLanguages.objects.create(name="English")
        # Create some TextbooksCategories objects associated with the language
        self.category1 = TextbooksCategories.objects.create(name="Math", language_associated=self.language)
        self.category2 = TextbooksCategories.objects.create(name="Science", language_associated=self.language)

    def test_class_categories_view(self):
        # Call the view function using the test client
        response = self.client.get(reverse('class_categories', args=['English']))

        # Check if the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Check if the all_categories is present in the context
        self.assertIn('all_categories', response.context)

        # Check if the number of all_categories matches the number of TextbooksCategories objects associated with the language
        all_categories = response.context['all_categories']
        self.assertEqual(all_categories.count(), TextbooksCategories.objects.filter(language_associated=self.language).count())

        # Check if the all_categories queryset contains the expected objects
        self.assertIn(self.category1, all_categories)
        self.assertIn(self.category2, all_categories)

class EducationViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # Create a sample EducationCategory
        self.category = EducationCategory.objects.create(name="Math", default=True)
        # Create some Education objects associated with the category
        self.post1 = Education.objects.create(title="Post 1")
        self.post2 = Education.objects.create(title="Post 2")
        # Associate the Education objects with the category using the .add() method
        self.post1.category.add(self.category)
        self.post2.category.add(self.category)

    def test_education_view_with_valid_category_id(self):
        # Call the view function using the test client with a valid category_id
        response = self.client.get(reverse('education', args=[self.category.id]))

        # Check if the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Check if the active_category is set correctly
        self.assertEqual(response.context['active_category'], self.category)

        # Check if all_post contains the expected Education objects associated with the category
        self.assertIn(self.post1, response.context['all_post'])
        self.assertIn(self.post2, response.context['all_post'])

        # Check if all_categories contains all EducationCategory objects
        self.assertEqual(set(response.context['all_categories']), set(EducationCategory.objects.all()))

    def test_education_view_with_invalid_category_id(self):
        # Call the view function using the test client with an invalid category_id
        response = self.client.get(reverse('education', args=[999]))

        # Check if the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Check if all_post is None
        self.assertIsNone(response.context['all_post'])

        # Check if all_categories contains all EducationCategory objects
        self.assertEqual(set(response.context['all_categories']), set(EducationCategory.objects.all()))


class ImpLinkViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.footer_link = FooterImportantLinks.objects.create(name="Sample Link", detail="Lorem Ipsum")

    def test_imp_link_view(self):
        response = self.client.get(reverse('imp_link', args=[self.footer_link.id]))

        self.assertEqual(response.status_code, 200)

        self.assertTemplateUsed(response, 'base/imp_link.html')

        self.assertIn('obj', response.context)

        self.assertEqual(response.context['obj'], self.footer_link)

class EducationPostViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # Create a sample Education object
        self.post = Education.objects.create(
            
            owner_or_institution_name = "Test",
            title = "Test",
            short_description = "Test",
            description = "Test",
            location = "Test",
            link_to_orignal = "Test",
        )

    def test_education_post_view(self):
        # Call the view function using the test client with the post_id
        response = self.client.get(reverse('education_post', args=[self.post.id]))

        # Check if the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Check if the post object is present in the context
        self.assertIn('post', response.context)

        # Check if the post object in the context matches the expected post object
        self.assertEqual(response.context['post'], self.post)


class CultureViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # Create sample CultureCategory objects
        self.category1 = CultureCategory.objects.create(name="Category 1", default=True)
        self.category2 = CultureCategory.objects.create(name="Category 2")
        # Create some Culture objects associated with the categories
        self.post1 = Culture.objects.create(title="Post 1", recommended=True, date=datetime.datetime(2024, 4, 1), description="Test")
        self.post2 = Culture.objects.create(title="Post 2", date=datetime.datetime(2024, 4, 2), description="Test")
        self.post3 = Culture.objects.create(title="Post 3", date=datetime.datetime(2024, 4, 3), description="Test")

        self.post1.category.add(self.category1)
        self.post2.category.add(self.category2)
        self.post3.category.add(self.category2)

    def test_culture_view_with_valid_category_id(self):
        # Call the view function using the test client with a valid category_id
        response = self.client.get(reverse('culture', args=[self.category1.id]))

        # Check if the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Check if the active_category is set correctly
        self.assertEqual(response.context['active_category'], self.category1)

        # Check if all_post contains the expected Culture objects associated with the category
        self.assertIn(self.post1, response.context['all_post'])

        # Check if recommended_post contains the recommended Culture object
        self.assertIn(self.post1, response.context['recommended_post'])

        # Check if upcomming_post does not contain the Culture objects with dates in the past
        self.assertNotIn(self.post1, response.context['upcomming_post'])

        # Optionally, you can check for the correctness of other context variables or template rendering

    def test_culture_view_with_invalid_category_id(self):
        # Call the view function using the test client with an invalid category_id
        response = self.client.get(reverse('culture', args=[999]))

        # Check if the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Check if all_post is None
        self.assertIsNone(response.context['all_post'])

        # Check if all_categories contains all CultureCategory objects
        self.assertEqual(set(response.context['all_categories']), set(CultureCategory.objects.all()))

class CulturePostViewTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        # Create a sample Culture object
        self.post = Culture.objects.create(title="Sample Post", short_description="Sample Content", description="Test", date=datetime.datetime.now())

    def test_culture_post_view(self):
        # Call the view function using the test client with the post_id
        response = self.client.get(reverse('culture_post', args=[self.post.id]))

        # Check if the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Check if the post object is present in the context
        self.assertIn('post', response.context)

        # Check if the post object in the context matches the expected post object
        self.assertEqual(response.context['post'], self.post)


class CreatePaymentIntentViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    @patch('stripe.PaymentIntent.create')
    def test_create_payment_intent_view(self, mock_create):
        # Mock the response from the Stripe API
        mock_create.return_value = {'client_secret': 'test_client_secret'}

        # Prepare POST data
        data = {
            'amount': 1000,
            'currency': 'usd',
            # Add other required fields as needed
        }

        # Call the view function using the test client with the prepared data
        response = self.client.post(reverse('create_payment_intent'), data=json.dumps(data), content_type='application/json')

        # Check if the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Check if the response contains the expected client secret
        content = json.loads(response.content)
        self.assertIn('clientSecret', content)
        self.assertEqual(content['clientSecret'], 'test_client_secret')

        # Check if stripe.PaymentIntent.create was called with the correct arguments
        mock_create.assert_called_once_with(amount=1000, currency='usd', automatic_payment_methods={'enabled': True})



class VerifyMyEmailViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='test_user', email='test@example.com', password='testpassword')

    def test_verify_my_email_view_with_valid_data(self):
        # Call the view function using the test client with valid user_id and username_code_only
        response = self.client.get(reverse('verify_my_email', args=[self.user.id, 'test_user']))

        # Check if the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Check if the user is activated and logged in
        self.user.refresh_from_db()  # Refresh user from database to get latest data
        self.assertTrue(self.user.is_active)
        self.assertTrue(self.user.is_authenticated)

        # Check if the final_str and return_url are as expected
        self.assertIn('final_str', response.context)
        self.assertIn('return_url', response.context)
        self.assertEqual(response.context['final_str'], 'Congrats')
        self.assertEqual(response.context['return_url'], settings.OSCAR_HOMEPAGE)

    def test_verify_my_email_view_with_invalid_data(self):
        # Call the view function using the test client with invalid user_id and username_code_only
        response = self.client.get(reverse('verify_my_email', args=[999, 'invalid_username_code']))

        # Check if the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Check if the final_str and return_url are as expected
        self.assertIn('final_str', response.context)
        self.assertIn('return_url', response.context)
        self.assertEqual(response.context['final_str'], 'Sorry')
        self.assertEqual(response.context['return_url'], '')

