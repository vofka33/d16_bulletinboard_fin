from celery import shared_task
import time

from django.core.mail import EmailMultiAlternatives, send_mail
from django.template.loader import render_to_string

from datetime import timedelta, date

from datetime import datetime, timezone

from .models import Post, User



@shared_task
def send_mail_every_week():
        news_post = []
        week_number_last = datetime.now().isocalendar()[1] - 1
        for post in Post.objects.filter(creation_date__week=week_number_last).values('pk', 'title', 'creation_date',):
            date_format = post.get("creation_date").strftime("%d/%m/%Y")
            new = (f'{post.get("title")}. '
                   f'Дата создания: {date_format}. Ссылка - http://127.0.0.1:8000/{post.get("pk")}')
            news_post.append(new)

        recipients = User.objects.all()
        if news_post:
            for recipient in recipients:
                send_mail(
                    subject=f'Celery. Новинки за неделю на BulletinBoard',
                    message=f"Здравствуйте, {recipient.username}. "
                            f' Публикации за неделю:\n {news_post} \n'
                            f'До встречи на нашем сайте!',
                    from_email=None,
                    recipient_list=[recipient.email]
                )


