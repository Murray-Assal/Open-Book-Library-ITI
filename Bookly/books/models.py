from django.db import models 
from django.shortcuts import reverse
from students.models import Student
from django.utils import timezone
from datetime import timedelta

class Book(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    cover = models.ImageField(upload_to='books/covers/',null=True,blank=True)
    author = models.CharField(max_length=100,null=True,blank=True)
    category = models.CharField(max_length=100,null=True,blank=True)
    published_date = models.DateField(null=True,blank=True)
    publisher = models.CharField(max_length=100,null=True,blank=True)
    
    def __str__(self):
        return self.title
    @property
    def image_url(self):
        return f'/media/{self.cover}'

    @property
    def show_url(self):
        url = reverse("books.show", args=[self.id])
        return url

    # @property
    # def borrow_url(self):
    #     url = reverse("books.borrow", args=[self.id])
    #     return url

class BorrowedBook(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE , null = True, blank = True, related_name='books')
    student = models.ForeignKey(Student, on_delete=models.CASCADE , null = True, blank = True, related_name='students')
    borrowed_date = models.DateField()
    return_date = models.DateField()
    
    def __str__(self):
        return self.book.title
    
    def save(self, *args, **kwargs):
        # Automatically set return_date to 2 weeks after borrow_date
        if self.borrowed_date and not self.return_date:
            self.return_date = self.borrowed_date + timedelta(weeks=2)
        super().save(*args,**kwargs)
    
    def image_url(self):
        return f'/media/{self.book.cover}'