from django.contrib.auth.tokens import default_token_generator
from django.urls import reverse
from oscar.apps.customer.utils import CustomerDispatcher as ParentCustomerDispatcher

import requests
import json

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
    


def send_message(receiver_phone, message, auth, sender_phone=None):
    """This function sends an SMS message to a given phone number

    Args:
        receiver_phone (str): receiver phone number in international format
        message (str): Message to be sent(should be maximum 160 characters)
        auth (str): authentication header value
        sender_phone (str, optional): Sender phone number. Should only come from api. Defaults to SENDER_PHONE.

    Returns:
        dict: Dictionary of return status code and response data from orange api
    """
    if sender_phone:
        url = f'https://api.orange.com/smsmessaging/v1/outbound/tel%3A%2B{sender_phone}/requests'
        headers = {
            "Content-Type" : "application/json",
            "Accept": 'application/json',
            "Authorization": auth
        }
        data = {
            "outboundSMSMessageRequest": {
                "address" : "tel:" + receiver_phone,
                "senderAddress": "tel:+" + sender_phone,
                "outboundSMSTextMessage": {
                    "message" : message
                }
            }
        }
        r = requests.post(url=url, data=json.dumps(data), headers=headers)
        return {
            "status": r.status_code,
            "content": r.json()
        }
    else:
        return None
    