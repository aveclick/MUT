from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Заголовок')
    slug = models.SlugField()
    intro = models.TextField(verbose_name='Интро')
    body = models.TextField(verbose_name='Содержание')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    img = models.ImageField(upload_to='img/', verbose_name='Фото', blank=True)

    class Meta:
        ordering = ['-date_added']


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    name = models.CharField(max_length=255, verbose_name='Имя')
    body = models.TextField(verbose_name='Комментарий')
    date_added = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')

    class Meta:
        ordering = ['-date_added']
