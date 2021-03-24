from django.contrib import admin
from p_library.models import Book, Author

# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass