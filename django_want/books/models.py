from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
from author.models import Author
from users.models import User


class Books(models.Model):
    """Модель описывающая книги"""

    author_id = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    book_caption = models.CharField(max_length=225)
    rating = models.IntegerField(validators=[MinValueValidator(0),
                                             MaxValueValidator(5)])
    create_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'


class Parts(models.Model):
    """Модель описания частей в книге"""
    book_id = models.ForeignKey(Books, on_delete=models.CASCADE)
    caption = models.CharField(max_length=255)
    order_id = models.IntegerField(default=0)

    class Meta:
        verbose_name = 'part'
        verbose_name_plural = 'parts'


class Chapters(models.Model):
    """Модель описание главы"""
    book_id = models.ForeignKey(Books, on_delete=models.CASCADE)
    part_id = models.ForeignKey(Parts, on_delete=models.CASCADE, blank=True, null=True, default=None)
    order_id = models.IntegerField(default=0)
    caption = models.CharField(max_length=255)
    description = models.TextField()

    class Meta:
        verbose_name = 'chapter'
        verbose_name_plural = 'chapters'
