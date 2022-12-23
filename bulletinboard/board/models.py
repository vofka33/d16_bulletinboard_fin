from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from django.urls import reverse


class Post(models.Model):
    TYPE = (
        ('tank', 'Танки'),
        ('heal', 'Хилы'),
        ('dd', 'ДД'),
        ('merchants', 'Торговцы'),
        ('guildmasters', 'Гилдмастеры'),
        ('questgivers', 'Квестгиверы'),
        ('blacksmiths', 'Кузнецы'),
        ('tanners', 'Кожевники'),
        ('potionmakers', 'Зельевары'),
        ('spellmasters', 'Мастера заклинаний'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=User, verbose_name="Автор")
    title = models.CharField(max_length=128, verbose_name="Заголовок объявления")
    text = RichTextUploadingField( blank=True, null=True, verbose_name="Текст объявления")
    category = models.CharField(max_length=16, choices=TYPE, default='tank', verbose_name="Категория")
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")

    def __str__(self):
        return f'{self.title}'

    def get_absolute_url(self):
        return f'http://127.0.0.1:8000/{self.id}'



class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=User, verbose_name="Автор комментария")
    text = models.TextField(verbose_name="Текст комментария")
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    creation_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата публикации")
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.post.title}'

    def accept(self):
        self.accepted = True
        self.save()

    def reject(self):
        self.accepted = False
        self.save()

    def get_absolute_url(self):
        return f'http://127.0.0.1:8000/{self.post.id}'



