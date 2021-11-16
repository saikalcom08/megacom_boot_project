from django.shortcuts import render
from .models import Books
from .models import ImageBook

# Create your views here.

def get_page_books(request):
    books = Books.objects.all()
    context = {
        'books': books
    }
    return render(request, 'all_books.html', context)
