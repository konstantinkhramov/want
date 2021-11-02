from django.db import models
from books.models.books import Books


class Chapters(models.Model):
    """Модель описание глав"""
    book = models.ForeignKey(Books,
                             related_name='chapters',
                             on_delete=models.CASCADE, blank=True, null=True, default=None)
    parent = models.ForeignKey('Chapters',
                               related_name='children',
                               on_delete=models.CASCADE,
                               blank=True,
                               null=True,
                               default=None)
    order = models.IntegerField(default=0)
    caption = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name = 'chapter'
        verbose_name_plural = 'chapters'
