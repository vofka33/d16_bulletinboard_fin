from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.
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
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    text = RichTextUploadingField('Текст', blank=True, null=True)
    category = models.CharField(max_length=16, choices=TYPE, default='tank')
    announced = models.BooleanField(default=False)
    dateCreation = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    # upload = models.FileField(upload_to='uploads/')


class Comment(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    text = models.TextField()
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    dateCreation = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    accepted = models.BooleanField(default=False)

