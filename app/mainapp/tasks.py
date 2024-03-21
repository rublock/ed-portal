import logging

from celery import shared_task
from django.core.mail import send_mail

logger = logging.getLogger(__name__)


@shared_task(bind=True)
def send_feedback_mail(self, user_message):
    logger.info(f"Message send: '{user_message}'")
    mail_subject = "ed_portal support message"
    send_mail(
        subject=mail_subject,
        message=user_message,
        from_email="lpsys1@gmail.com",
        recipient_list=['lpsys1@gmail.com'],
        fail_silently=False,
    )
    return "Done"
