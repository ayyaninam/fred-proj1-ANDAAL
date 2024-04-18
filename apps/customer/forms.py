from django import forms
from django.utils.translation import gettext_lazy as _
from oscar.core.compat import get_user_model
from oscar.apps.customer.forms import EmailUserCreationForm as ParentEmailUserCreationForm
from oscar.apps.customer.forms import generate_username
from .models import *
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from oscar.apps.customer.utils import normalise_email
from django.contrib.sites.shortcuts import get_current_site
from oscar.apps.customer.utils import get_password_reset_url, normalise_email
from oscar.apps.customer.forms import EmailAuthenticationForm as ParentEmailAuthenticationForm
from oscar.apps.customer.forms import PasswordResetForm as ParentPasswordResetForm
from oscar.core.loading import get_class
User = get_user_model()

CustomerDispatcher = get_class("customer.utils", "CustomerDispatcher")

class EmailAuthenticationForm(ParentEmailAuthenticationForm):
    username = forms.CharField(label=_("Email address/Phone Number"), help_text="Use your Country Code if you want to login with your Phone Number e.g:(+237)")

    def clean_username(self):
        username = self.cleaned_data["username"]
        if ('+237' in username) and ('@dummy.skip' not in username):
            username = f"{username}@dummy.skip"

        return username


class EmailUserCreationForm(ParentEmailUserCreationForm):
    email = forms.EmailField(label=_("Email address"), required=False)
    phone_number = PhoneNumberField(required=True, widget=PhoneNumberPrefixWidget(initial='CM', attrs={'style':'display:inline-block; width:50%'}))


    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'phone_number')


    def clean(self):
        phone_number = self.cleaned_data.get("phone_number", "")
        email = self.cleaned_data.get("email", '')
        
        if not (phone_number):
            raise forms.ValidationError(
                _("Please Enter a Phone Number")
            )
        
        if not (str(phone_number).startswith('+237')):
            if (email == ""):
                self.add_error("email", "Please Provide us an Email, if you aren't use Cameroon +237 Phone Number")
      
        if User._default_manager.filter(phone_number__iexact=str(phone_number)).exists(): 
            raise forms.ValidationError(
                _("A user with same Phone Number already exists")
            )
        
        if not email:
            email = normalise_email(f"{self.cleaned_data.get('phone_number')}@dummy.skip")


        self.cleaned_data.update({'email':email})

    def clean_email(self):
        """
        Checks for existing users with the supplied email address.
        """
        email = normalise_email(self.cleaned_data["email"])

        if (email!=""):
            if User._default_manager.filter(email__iexact=email).exists():
                raise forms.ValidationError(
                    _("A user with that email address already exists")
                )

        return email
    

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        if "username" in [f.name for f in User._meta.fields]:
            user.username = f'{generate_username()}--{self.clean_redirect_url()}'
        if commit:
            user.save()
        return user
    

from django.conf import settings
from .utils import send_message

class PasswordResetForm(ParentPasswordResetForm):
    email = forms.CharField(
            label=_("Email/Phone Number"),
            max_length=254,
            # widget=forms.EmailInput(attrs={"autocomplete": "email"}),
        )
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if ('+237' in email) and ('@dummy.skip' not in email):
            email = f"{email}@dummy.skip"
        return email

    def send_password_reset_email(self, site, user, request=None):
        if user.email.find("dummy.skip") != -1:
            extra_context = {"user": user, "request": request}
            send_message(str(user.phone_number), CustomerDispatcher().get_password_reset_email_for_user(user, extra_context)['body'], settings.SMS_AUTH_SCRETE_KEY, settings.SMS_SENDER_PHONE_NUMBER)
        else:
            extra_context = {
                "user": user,
                "site": site,
                "reset_url": get_password_reset_url(user),
                "request": request,
            }
            CustomerDispatcher().send_password_reset_email_for_user(user, extra_context)