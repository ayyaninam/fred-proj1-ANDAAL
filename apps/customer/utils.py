from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from oscar.apps.customer.utils import CustomerDispatcher as ParentCustomerDispatcher

class CustomerDispatcher(ParentCustomerDispatcher):

    def get_registration_email_for_user(self, user, extra_context):
        messages = self.dispatcher.get_messages(
            self.REGISTRATION_EVENT_CODE, extra_context
        )
        return messages

    def get_password_reset_email_for_user(self, user, extra_context):
        messages = self.dispatcher.get_messages(
            self.PASSWORD_RESET_EVENT_CODE, extra_context
        )
        return messages

    def get_password_changed_email_for_user(self, user, extra_context):
        messages = self.dispatcher.get_messages(
            self.PASSWORD_CHANGED_EVENT_CODE, extra_context
        )
        return messages

    def get_email_changed_email_for_user(self, user, extra_context):
        messages = self.dispatcher.get_messages(
            self.EMAIL_CHANGED_EVENT_CODE, extra_context
        )
        return messages