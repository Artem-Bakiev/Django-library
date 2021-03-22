from django.shortcuts import render

# Create your views here.
def books_list(request):
    books = Book.objects.all()
    return HttpResponse(books)