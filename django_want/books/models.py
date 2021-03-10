from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
from users.models import User


class Books(models.Model):
    """Модель описывающая книги"""
    author_id = models.ForeignKey(User, on_delete=models.CASCADE)
    book_caption = models.CharField(max_length=225)
    author_book_name = models.CharField(max_length=225)
    rating = models.IntegerField(validators=[MinValueValidator(0),
                                             MaxValueValidator(5)])
    create_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField()


class Chapters(models.Model):
    """Модель описание главы"""
    book_id = models.ForeignKey(Books, on_delete=models.CASCADE)
    caption = models.CharField(max_length=255)
    description = models.TextField()
