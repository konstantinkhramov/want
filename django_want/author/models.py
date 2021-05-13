from django.db import models

# Create your models here.


class Author(models.Model):
    """Модель описывающая автора книги"""

    name = models.CharField(max_length=140)
    last_name = models.CharField(max_length=140)
    middle_name = models.CharField(max_length=140, null=True)
    year_of_bird = models.DateField(null=True)

    class Meta:
        verbose_name = 'author'
        verbose_name_plural = 'authors'
