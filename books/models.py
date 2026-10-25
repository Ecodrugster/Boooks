from django.db import models

class Book(models.Model):
    title = models.CharField('Название', max_length=200)
    author = models.CharField('Автор', max_length=200)
    description = models.TextField('Описание')
    is_read = models.BooleanField('Прочитана', default=False)

    class Meta:
        ordering = ['-id']
        verbose_name = 'книга'
        verbose_name_plural = 'книги'

    def __str__(self):
        return self.title
