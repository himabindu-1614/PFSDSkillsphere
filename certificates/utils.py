from django.core.mail import send_mail
from datetime import date, timedelta
from .models import Certificate


def send_expiry_alerts():
    target_date = date.today() + timedelta(days=7)

    certs = Certificate.objects.filter(expiry_date=target_date)

    for cert in certs:
        send_mail(
            subject="Certificate Expiry Alert ⚠️",
            message=f"Your certificate '{cert.title}' is expiring in 7 days.",
            from_email="your_email@gmail.com",
            recipient_list=[cert.user.email],
        )