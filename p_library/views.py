from django.shortcuts import render
from django.http import HttpResponse
from p_library.models import Book

# Create your views here.
def books_list(request):
    books = Book.objects.all()
    return HttpResponse(books)