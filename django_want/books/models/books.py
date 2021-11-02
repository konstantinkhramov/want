from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.
from author.models import Author
from users.models import User


class Books(models.Model):
    """Модель описывающая книги"""

    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    book_caption = models.CharField(max_length=225)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], null=True, blank=True)
    create_date = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True)

    class Meta:
        verbose_name = 'book'
        verbose_name_plural = 'books'
