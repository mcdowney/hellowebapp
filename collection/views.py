from django.shortcuts import render
from collection.models import Book

# Create your views here.
def index(request):
	# This is your new view
	books = Book.objects.all()
	return render(request, 'index.html', {
		'books': books,
	})

def book_detail(request, slug):
	# grab the object...
	book = Book.objects.get(slug=slug)
	# and pass it to the template.
	return render(request, 'books/book_detail.html', {
		'book': book,
		})