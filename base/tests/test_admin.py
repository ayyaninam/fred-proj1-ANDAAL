from django.test import TestCase
from django.contrib.admin.sites import AdminSite

from base.models import Education
from base.admin import duplicate_selected
from django.contrib.auth import get_user_model

User = get_user_model()


class EducationAdminTestCase(TestCase):
    def setUp(self):
        self.admin_site = AdminSite()
        self.user = User.objects.create_superuser(username='admin', email='admin@example.com', password='password')

    def test_duplicate_selected(self):
        education = Education.objects.create(title="Sample Education Title", description="Sample Description")

        duplicate_selected(modeladmin=None, request=None, queryset=Education.objects.filter(pk=education.pk))

        duplicated_education = Education.objects.filter(title="Sample Education Title").exclude(pk=education.pk).first()
        self.assertNotEqual(education.pk, duplicated_education.pk)
        self.assertEqual(education.title, duplicated_education.title)
        self.assertEqual(education.description, duplicated_education.description)
