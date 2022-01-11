from django.views.generic import ListView
from.models import Book
class BookList(ListView): 
    model = Book