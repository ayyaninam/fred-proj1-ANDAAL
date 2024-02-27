from django import forms
from django.utils.translation import gettext_lazy as _
from oscar.core.compat import existing_user_fields, get_user_model
from oscar.apps.customer.forms import EmailUserCreationForm as ParentEmailUserCreationForm
from oscar.apps.customer.forms import generate_username
from .models import *
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget
from oscar.apps.customer.utils import get_password_reset_url, normalise_email
from django.core.exceptions import ValidationError
from django.contrib.auth.password_validation import validate_password



User = get_user_model()

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
      
        if User._default_manager.filter(phone_number__iexact=phone_number).exists(): 
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
            user.username = generate_username()
        if commit:
            user.save()
        return user
