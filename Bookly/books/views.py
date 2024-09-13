from django.shortcuts import render, redirect, reverse, get_object_or_404
from books.models import Book
from books.forms import BookForm, BorrowedBookForm
from books.models import BorrowedBook
from django.views.generic import CreateView, UpdateView, FormView , DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from  students.models import Student

def home(request):
    # Assuming related_name='borrowed_books' is set in the ForeignKey field
    books_not_borrowed = Book.objects.exclude(books__isnull=False)
    return render(request, 'books/home.html', {'books': books_not_borrowed})

def index(request):
    books = Book.objects.all()
    return render(request, 'books/books_index.html', {'books': books})

class BookLoanConfirmView(FormView):
    form_class = BorrowedBookForm
    template_name = 'books/borrow_book.html'
    success_url = '/books/home'  # Redirect to a success page

    def form_valid(self, form):
        # Create a new BookLoan instance
        book_loan = BorrowedBook(borrowed_date=timezone.now().date(), book_id=self.kwargs['id'], student_id=self.request.user.id)
        book_loan.save()
        return super().form_valid(form)
    

def show(request,id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'books/show.html', {'book' : book})

class CreateBookView(LoginRequiredMixin, CreateView):
    model = Book
    form_class = BookForm
    template_name = 'books/create.html'
    success_url = '/books/index'

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class UpdateBookView(LoginRequiredMixin, UpdateView):
    model = Book
    form_class = BookForm
    template_name = 'books/edit.html'
    success_url = '/books/index' 

def delete(request,id):
    book = get_object_or_404(Book, id=id)
    book.delete()
    return redirect(reverse("books.index"))

def show_student_books(request):
    borrowed_books = BorrowedBook.objects.filter(student_id=request.user.id)
    return render(request, 'students/student_books.html', {'books': borrowed_books})

def returnbook(request,id):
    book = get_object_or_404(BorrowedBook, id=id)
    book.delete()
    return redirect(reverse("books.student_books"))

# def books_by_author(request,name):
#     result = Book.objects.filter(author=name)
#     return render(request, 'books/books_author.html', {'books': result})


# def books_by_category(request,category):
#     result = Book.objects.filter(category=category)
#     return render(request, 'books/books_category.html', {'books': result})