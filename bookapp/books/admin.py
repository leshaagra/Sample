from django.contrib import admin
from .models import Book

admin.site.register(Book)

# @admin.register(Book)
# class BookAdmin(admin.ModelAdmin):
#     list_display = ('title', 'author', 'published_date')  # Ensure 'published_date' is a valid field
#     search_fields = ('title', 'author')
#     list_filter = ('published_date',)  # Ensure 'published_date' is a valid field
