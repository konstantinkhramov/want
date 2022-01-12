# Generated by Django 3.1 on 2021-11-16 19:06

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('author', '0002_author_year_of_bird_null_true'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_caption', models.CharField(max_length=225)),
                ('rating', models.IntegerField(blank=True, null=True,
                                               validators=[django.core.validators.MinValueValidator(0),
                                                           django.core.validators.MaxValueValidator(5)])),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField(blank=True)),
                ('author', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL,
                                             to='author.author')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'book',
                'verbose_name_plural': 'books',
            },
        ),
        migrations.CreateModel(
            name='Chapters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(default=0)),
                ('caption', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('parent',
                 models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE,
                                   related_name='children', to='books.chapters')),
                ('book',
                 models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE,
                                   related_name='chapters', to='books.books')),
            ],
            options={
                'verbose_name': 'chapter',
                'verbose_name_plural': 'chapters',
            },
        ),
    ]