# blog/utils.py
from django.core.mail import send_mail
from django.conf import settings

def send_notification_email(user, action):
    subject = f'Account Notification: {action}'
    message = f'Dear {user.username}, your account has been {action}.'
    
    send_mail(
        subject,
        message,
        settings.DEFAULT_FROM_EMAIL,
        [user.email],
        fail_silently=False,
    )
