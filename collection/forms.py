from django.forms import ModelForm
from collection.models import Book

class BookForm(ModelForm):
	class Meta:
		model = Book
		fields = ('name', 'description',)