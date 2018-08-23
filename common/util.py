from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template


def email_user(subject, context, text_template_path, html_template_path):
    """
    Dispatch a notification email to a user.

    Args:
        subject (str): Email subject - required
        context (str): Email context - required
        text_template_path (str): text_template_path - required
        html_template_path (str): html_template_path - required
    """
    text_template = get_template(text_template_path)
    html_template = get_template(html_template_path)
    html_alternative = html_template.render(context)
    text_alternative = text_template.render(context)
    email = EmailMultiAlternatives(
        subject,
        text_alternative,
        settings.DEFAULT_FROM_EMAIL,
        [context['to']],
        bcc=[settings.DEFAULT_BCC_EMAIL],
    )
    email.attach_alternative(html_alternative, "text/html")
    email.send(fail_silently=False)