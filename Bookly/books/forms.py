from books.models import *
from django import forms

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class BorrowedBookForm(forms.Form):
    confirm = forms.BooleanField(label='Are you sure you want to borrow this book?', required=True)