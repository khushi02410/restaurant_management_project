import string , secrets , logging
from django.core.mail import send_mail
from django.conf import settings
from .models import Coupon, Order
from django.db.models import Sum

def generate_coupon_code(length=10):
    characters = string.ascii_uppercase + string.digits
    while True:
        code = ''.join(secrets.choice(characters) for _ in range(length))
        if not Coupon.objects.filter(code=code).exists():
            return code

logger = logging.getLogger(__name__)

def send_order_confirmation_email(order_id, customer_email, customer_name=None):
    try:
        subject = f"Order Confirmation - #{order_id}"
        message = (
            f"Hello {customer_name or 'customer'},\n\n"
            f"Thank you for your order!\n"
            f"Your order ID is #{order_id}.\n\n"
            f"Best regards,\nThe Shop Team"
        )
        from_email = settings.DEFAULT_FROM_EMAIL  # Make sure it's set in settings.py
        recipient_list = [customer_email]

        send_mail(subject, message, from_email, recipient_list, fail_silently=False)
        return True
    except Exception as e:
        logger.error(f"Email sending failed: {str(e)}")
        return False

def daily_sales_total(date):
    try:
        orders = Order.objects.filter(created_at__date=date)
        
        total_sales = orders.aggregate(total_sum=Sum('total_price'))['total_sum']

        # Return total or 0 if None
        return total_sales or 0
    except Exception as e:
        print(f"Error calculating daily sales: {e}")
        return 0       
    
def generate_unique_order_id(length=9):
    characters = string.ascii_uppercase + string.digits

    while True:
        unique_id = ''.join(secrets.choice(characters) for _ in range(length))
        if not Order.objects.filter(order_id=unique_id).exists():
            return unique_id   