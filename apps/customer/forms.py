from django import forms
from django.utils.translation import gettext_lazy as _
from oscar.core.compat import existing_user_fields, get_user_model
from oscar.apps.customer.forms import EmailUserCreationForm as ParentEmailUserCreationForm
from oscar.apps.customer.forms import generate_username

User = get_user_model()


class EmailUserCreationForm(ParentEmailUserCreationForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])

        if "username" in [f.name for f in User._meta.fields]:
            user.username = generate_username()
        if commit:
            user.save()

        return user