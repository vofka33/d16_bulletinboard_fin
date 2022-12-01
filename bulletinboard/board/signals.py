from .models import Comment

from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string


@receiver(post_save, sender=Comment)
def comment_notify(sender, instance, created, **kwargs):
    if instance.accepted:
        subject = f'{instance.author}, ваш комментарий опубликован'
        body = f'Здравствуйте, {instance.author}! Ваш комментарий от {instance.creation_date.strftime("%d-%m-%Y")} к публикации "{instance.post.title}" пользователя {instance.post.author} опубликован.'
        email = instance.author.email

    if not instance.accepted:
        subject = f'{instance.author}, ваш комментарий был отклонен'
        body = f'Здравствуйте {instance.author}, комментарий от {instance.creation_date.strftime("%d-%m-%Y")} к публикации "{instance.post.title}" пользователя {instance.post.author} был отклонен.'
        email = instance.author.email

    if created:
        subject = f'К вашей публикации "{instance.post.title}" добавлен новый комментарий'
        body = f'Здравствуйте {instance.post.author}! Вы получили комментарий к вашей публикации "{instance.post.title}" от пользователя {instance.author}, {instance.creation_date.strftime("%d-%m-%Y %H:%M")}'
        email = instance.post.author.email

    msg = EmailMultiAlternatives(
        subject=subject,
        body=body,
        from_email=None,
        to=[email]
    )

    html_content = render_to_string(
        'comment_created.html',
        {
            'comment': instance,
            'body': body
        }
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()


@receiver(post_delete, sender=Comment)
def delete_comment_notify(sender, instance, **kwargs):
    subject = f'{instance.author}, ваш комментарий был удален'
    body = f'Здравствуйте, {instance.author}! Ваш комментарий от {instance.creation_date.strftime("%d-%m-%Y")} к публикации "{instance.post.title}" автора {instance.post.author} был удален.'
    email = instance.author.email

    msg = EmailMultiAlternatives(
        subject=subject,
        body=body,
        from_email=None,
        to=[email]
    )

    html_content = render_to_string(
        'comment_created.html',
        {
            'comment': instance,
            'body': body
        }
    )
    msg.attach_alternative(html_content, "text/html")
    msg.send()