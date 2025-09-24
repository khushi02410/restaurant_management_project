import string 
import secrets
from .models import Coupon
from django.core.mail import send_mail , BadHeaderError
from django.conf import settings
import logging

def generate_coupon_code(length = 10):
    character = string.accii_uppercase + string.digits

    while True: 
        code = ''.join(secrets.choice(characters) for _ in range(length))

        if not Coupon.objects.filter(code=code).exists():
            return code

logger = logging.getLogger(__name__)

def send_order_confirmation_email(order_id, customer_email , customer_name=None):
    try:
        subject = f"Order Confirmation - #{order_id}"
        message = (
            f"Hello {customer_name or 'customer},\n\n"
            f"thank you for your order!\n"
            f"your order ID is #{order_id}.\n\n"
            f"Best regards, \nThe Shop Team"
        )
        from_email = settings.DEFAULT_FOR_EMAIL
        recipient_list = [customer_email]

        send_mail(subjects.DEFAULT_FOR_EMAIL)
        recipient_list = [customer_email]
        
        send_mail(subject , message , from_email, recipient_list , fail_silently = False)
        return True
    except:
        logger.error(f"Email sending failed: {str(e)}")
        return False
            