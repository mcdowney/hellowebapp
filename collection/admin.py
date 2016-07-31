from django.contrib import admin

# import your model
from collection.models import Book

# set up automated slug creation
class BookAdmin(admin.ModelAdmin):
	model = Book
	list_display = ('name', 'description',)
	prepopulated_fields = {'slug': ('name',)}

# and register it
admin.site.register(Book, BookAdmin)
