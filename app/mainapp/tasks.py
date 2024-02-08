from celery import shared_task
from django.core.mail import send_mail


@shared_task(bind=True)
def send_feedback_mail(self, user_message, user_mail):
    mail_subject = "ed_portal support message"
    send_mail(
        subject=mail_subject,
        message=user_message,
        from_email="lpsys1@gmail.com",
        recipient_list=[user_mail],
        fail_silently=False,
    )
    return "Done"
