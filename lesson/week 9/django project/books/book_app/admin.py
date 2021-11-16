from django.contrib import admin
from .models import Books, Author, ImageBook


admin.site.register(Books)
admin.site.register(Author)
admin.site.register(ImageBook)
