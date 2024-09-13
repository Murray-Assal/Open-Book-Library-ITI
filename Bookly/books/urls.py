from django.urls import path, include
from books.views import *
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path('home/',home,name='books.home'),
    path('index/',index,name='books.index'),
    path('show/<int:id>',show,name='books.show'),
    path('create/',login_required(CreateBookView.as_view()),name='books.create'),
    path('edit/<int:pk>',login_required(UpdateBookView.as_view()),name='books.edit'),
    path('delete/<int:id>',login_required(delete),name='books.delete'),
    path('student_books/',login_required(show_student_books),name='books.student_books'),
    path('return/<int:id>',login_required(returnbook),name='books.return'),
    # path('borrow/<int:id>',borrow_book,name='books.borrow'),
    path('borrow/<int:id>',login_required(BookLoanConfirmView.as_view()),name='books.borrow'),
    # path('author/<str:name>/',books_by_author,name='books.author'),
    # path('category/<str:category>/',books_by_category,name='books.category'),
]