from django.test import TestCase, RequestFactory
from django.urls import reverse
from base.models import FooterImportantLinks

from django.contrib.auth import get_user_model
User = get_user_model()

class ImpLinkViewTestCase(TestCase):
    def setUp(self):
        # Create a sample FooterImportantLinks object
        self.footer_link = FooterImportantLinks.objects.create(name="Sample Link", url="/sample-link/")

    def test_imp_link_view(self):
        # Create a request object
        request = RequestFactory().get(reverse('imp_link', args=[self.footer_link.id]))

        # Call the view function
        response = imp_link(request, self.footer_link.id)

        # Check if the response status code is 200
        self.assertEqual(response.status_code, 200)

        # Check if the correct template is used
        self.assertTemplateUsed(response, 'base/imp_link.html')

        # Check if the object is present in the context
        self.assertIn('obj', response.context)

        # Check if the object in the context matches the created FooterImportantLinks object
        self.assertEqual(response.context['obj'], self.footer_link)
