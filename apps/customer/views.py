import requests
import json
from django.conf import settings
from oscar.apps.customer.views import AccountAuthView as ParentAccountAuthView
from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth import authenticate


class AccountAuthView(ParentAccountAuthView):
    def get_registration_success_url(self, form):
        return settings.LOGIN_REDIRECT_URL
    