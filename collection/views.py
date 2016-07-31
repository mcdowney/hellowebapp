from django.shortcuts import render
from collection.models import Book

# Create your views here.
def index(request):
	# This is your new view
	books = Book.objects.all()
	return render(request, 'index.html', {
		'books': books,
	})