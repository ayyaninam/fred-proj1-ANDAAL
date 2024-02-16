import logging

from django.conf import settings
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login

from oscar.apps.customer.signals import user_registered
from oscar.core.compat import get_user_model
from oscar.core.loading import get_class, get_model
from oscar.apps.customer.mixins import RegisterUserMixin as ParentRegisterUserMixin
User = get_user_model()
CommunicationEventType = get_model("communication", "CommunicationEventType")
CustomerDispatcher = get_class("customer.utils", "CustomerDispatcher")

logger = logging.getLogger("oscar.customer")


class RegisterUserMixin(ParentRegisterUserMixin):
    def register_user(self, form):
        """
        Create a user instance and send a new registration email (if configured
        to).
        """
        user = form.save()

        # Raise signal robustly (we don't want exceptions to crash the request
        # handling).
        user_registered.send_robust(sender=self, request=self.request, user=user)

        if getattr(settings, "OSCAR_SEND_REGISTRATION_EMAIL", True):
            if user.email.find("dummy.skip") != -1:
                logger.warning("WE WILL SEND YOU AN SMS")
            else:
                self.send_registration_email(user)

        # We have to authenticate before login
        try:
            user = authenticate(
                username=user.email, password=form.cleaned_data["password1"]
            )
        except User.MultipleObjectsReturned:
            # Handle race condition where the registration request is made
            # multiple times in quick succession.  This leads to both requests
            # passing the uniqueness check and creating users (as the first one
            # hasn't committed when the second one runs the check).  We retain
            # the first one and deactivate the dupes.
            logger.warning(
                "Multiple users with identical email address and password"
                "were found. Marking all but one as not active."
            )
            # As this section explicitly deals with the form being submitted
            # twice, this is about the only place in Oscar where we don't
            # ignore capitalisation when looking up an email address.
            # We might otherwise accidentally mark unrelated users as inactive
            users = User.objects.filter(email=user.email)
            user = users[0]
            for u in users[1:]:
                u.is_active = False
                u.save()

        # auth_login(self.request, user)
        user.is_active = False
        user.save()
        return user

    def send_registration_email(self, user):
        extra_context = {"user": user, "request": self.request}
        CustomerDispatcher().send_registration_email_for_user(user, extra_context)
