from django.shortcuts import render, redirect
from collection.forms import BookForm
from collection.models import Book
from django.template.defaultfilters import slugify
from django.contrib.auth.decorators import login_required
from django.http import Http404

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
@login_required
def edit_book(request, slug):
	# grab the object...
	book = Book.objects.get(slug=slug)

	# make sure the logged in user is the owner of the thing
	if book.user != request.user:
		raise Http404

	# set the form we're using...
	form_class = BookForm
	# if we're coming to this view from a submitted form.
	if request.method == 'POST':
		# grab the data from the submitted form
		form = form_class(data=request.POST, instance=book)
		if form.is_valid():
			#save the new data
			form.save()
			return redirect('book_detail', slug=book.slug)
	# otherwise, just create the form
	else: 
		form = form_class(instance=book)

	# and render the template
	return render(request, 'books/edit_book.html', {
		'book': book,
		'form': form,
	})

def create_book(request):
	form_class = BookForm
	if request.method == 'POST':
		form = form_class(request.POST)
		if form.is_valid():
			book = form.save(commit=False)
			book.user = request.user
			book.slug = slugify(book.name)
			book.save()
			return redirect('book_detail', slug=book.slug)

	else:
		form = form_class()

	return render(request, 'books/create_book.html', {
		'form': form,
			})