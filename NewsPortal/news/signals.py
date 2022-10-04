from django.db.models.signals import m2m_changed
from django.dispatch import receiver  # импортируем нужный декоратор
from django.core.mail import EmailMultiAlternatives  # импортируем класс для создание объекта письма с html
from django.template.loader import render_to_string  # импортируем функцию, которая срендерит наш html в текст
from .models import PostCategory, CategorySubscribers
from NewsPortal.settings import DEFAULT_FROM_EMAIL  # для почтового ящика по умолчанию


@receiver(m2m_changed, sender=PostCategory)
def notify_post_create(sender, instance, action, **kwargs):
    if action == 'post_add':
        for cat in instance.postCategory.all():
            for subscribe in CategorySubscribers.objects.filter(category_thru=cat):

                msg = EmailMultiAlternatives(
                    subject=instance.title,
                    body=instance.text,
                    from_email=DEFAULT_FROM_EMAIL,
                    to=[subscribe.subscriber_thru.email],
                )

                html_content = render_to_string(
                    'newpost.html',
                    {
                        'title': instance.title,
                        'posts': instance.text,
                        'recipient': subscribe.subscriber_thru.email,
                        'category_name': subscribe.category_thru,
                        'subscriber_user': subscribe.subscriber_thru,
                        'pk_id': instance.pk,
                    },
                )

                msg.attach_alternative(html_content, "text/html")
                msg.send()