from django.contrib import admin
from .models import Books, Chapters, Parts

# Register your models here.
admin.site.register(Books)
admin.site.register(Chapters)
admin.site.register(Parts)
