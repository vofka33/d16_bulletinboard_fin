from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

from ckeditor.fields import RichTextField


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
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=User)
    title = models.CharField('Заголовок ', max_length=128)
    text = RichTextUploadingField('Текст', blank=True, null=True)
    category = models.CharField(max_length=16, choices=TYPE, default='tank')
    announced = models.BooleanField(default=False)
    header_image = models.FileField(null=True, blank=True, upload_to='images/')
    сreation_date = models.DateTimeField('Дата публикации ', auto_now_add=True)



class Comment(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)

