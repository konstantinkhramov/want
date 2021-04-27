# Generated by Django 3.1 on 2021-03-10 19:46

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_caption', models.CharField(max_length=225)),
                ('author_book_name', models.CharField(max_length=225)),
                ('rating', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(5)])),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('description', models.TextField()),
                ('author_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Chapters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('book_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.books')),
            ],
        ),
    ]